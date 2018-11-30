from datetime import datetime

SECOND = 1
MINUTES = 60 * SECOND
HOUR = 60 * MINUTES
DAY = 24 * HOUR
MONTH = 30.436875
YEAR = 365.2425

date1 = 'April 12, 1961 2:07 local time'  # Asia/Almaty
out1 = datetime.strptime(date1, '%B %d, %Y %H:%M local time')
print(f'Now is {out1:%Y-%m-%dT%H:%M:%S}!')

date2 = '"07/21/69 2:56:15 AM UTC"'
out2 = datetime.strptime(date2, '\"%m/%d/%y %I:%M:%S %p %Z\"')
print(f'Now is {out2:%Y-%m-%dT%H:%M:%S}!')


def roznica_czasu(date1, date2):
    duration = date2 - date1
    years, days = divmod(duration.days, YEAR)
    months, days = divmod(days, MONTH)
    hours, minutes = divmod(duration.seconds, HOUR)
    minutes, seconds = divmod(minutes, MINUTES)
    return
