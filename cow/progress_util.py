import sys


import time
import sys

def progress(progress):
    print('\r[{0}] {1}%'.format('#'*int(progress/2), progress))
#
# def progress(count, total, status=''):
#     bar_len = 60
#     filled_len = int(round(bar_len * count / float(total)))
#
#     percents = round(100.0 * count / float(total), 1)
#     bar = '=' * filled_len + '-' * (bar_len - filled_len)
#
#     sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
#     sys.stdout.flush()
#     import time
#     time.sleep(.1)