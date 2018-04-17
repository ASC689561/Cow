import logging
import traceback
from functools import wraps

SUCCESS = 200  # thành công
UNKNOWN_EXCEPTION = 201  # lỗi unknown
TOKEN_INVALID = 202  # sai token


class WebServiceException:
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


def auto_try_catch(method):
    @wraps(method)
    def try_catch(*args, **kw):
        from flask import jsonify

        try:
            result = method(*args, **kw)
            return jsonify({'code': SUCCESS, 'status': 'success', 'data': result, 'message': None})
        except Exception as ex:
            logging.error(traceback.format_exc())
            code = ex.__dict__.get('code', None)
            if code is not None:
                return jsonify({'code': code, 'status': 'error', 'data': None, 'message': str(ex)})
            return jsonify({'code': UNKNOWN_EXCEPTION, 'status': 'error', 'data': None, 'message': str(ex)})

    return try_catch
