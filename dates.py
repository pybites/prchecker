import calendar
from datetime import datetime

NOW = datetime.now()
HACKTOBER_RANGE = ('2017-09-30T00:00:00-12:00'
                   '..'
                   '2017-10-31T23:59:59-12:00')
MONTH_INT_TO_NAME = {k: v for k, v in
                     enumerate(calendar.month_name)}


def get_date_range(month, hacktober_range=False):
    '''Get date range (start-end day) of month
       Call with hacktober_range=True to match Digital Ocean's
       more inclusive Hacktoberfest range for Oct'''
    try:
        month = int(month)
    except ValueError:
        month = NOW.month

    if month not in range(1, 13):
        month = NOW.month

    if month == 10 and hacktober_range:
        return HACKTOBER_RANGE

    _, end_day = calendar.monthrange(NOW.year, month)
    yymm = '{}-{}-'.format(NOW.year, str(month).zfill(2))
    return '{0}01..{0}{1}'.format(yymm, end_day)
