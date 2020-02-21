import datetime

# printing the current date and time
# to get a
now = datetime.datetime.now()
date_now = now.date()
time_now = now.time()
print('\nnow: ', now)
print('only time now: ', time_now)
print('only date now: ', date_now)
print('year: ', now.year)
print('month: ', now.month)
print('day: ', now.day)
print('hour: ', now.hour)
print('minute:', now.minute)
print('second: ', now.second)
print('microsecond: ', now.microsecond)

# setting a start date for an event
start_year = 2009
start_month = 4
start_day = 1
start_hour = 10
start_minute = 30
start_second = 0
start_microsecond = 0

# I could replace the 'now' values like that
# I could replace only the values I want (not necessary to change all)
start_datetime = now.replace(
    year=start_year,
    month=start_month,
    day=start_day,
    hour=start_hour,
    minute=start_minute,
    second=start_second,
    microsecond=start_microsecond
    )
print('\nstart date and time: ',start_datetime)

workingtime = datetime.datetime.now() - start_datetime # returns datetime.timedelta(days, seconds, microseconds)
days_workingtime = workingtime.days
seconds_workingtime = workingtime.seconds
microseconds_workingtime = workingtime.microseconds
hours_workingtime = seconds_workingtime/3600
minutes_workingtime = 60*(hours_workingtime - int(hours_workingtime)) # i.e. 23.75 hours = 23.75 - 23 = 0.75*60 minutes

print(
    '\ntime working:\n'
    '{} days\n'
    '{} seconds\n'
    '{} microseconds'.format(days_workingtime, seconds_workingtime, microseconds_workingtime))

# to ckeck, use
# https://www.timeanddate.com/date/timeduration.html?d1=01&m1=04&y1=2009&d2=21&m2=02&y2=2020&h1=10&i1=30&s1=0&h2=10&i2=15&s2=0&
print(
    '\ntime working in another format:\n'
    '{} days\n'
    '{} hours\n'
    '{} minutes\n'.format(days_workingtime, int(hours_workingtime), int(minutes_workingtime)))

#---------- working with datetime.timedelta --------------------
# add time to a time that was setted
time_to_add = datetime.timedelta(days=4, hours=2, seconds=25) 
new_workingtime = workingtime + time_to_add

days_workingtime = new_workingtime.days
seconds_workingtime = new_workingtime.seconds
microseconds_workingtime = new_workingtime.microseconds
hours_workingtime = seconds_workingtime/3600
minutes_workingtime = 60*(hours_workingtime - int(hours_workingtime)) # i.e. 23.75 hours = 23.75 - 23 = 0.75*60 minutes

print(
    '\ntime working with plus 4 days and 2 hours, 25 seconds:\n'
    '{} days\n'
    '{} hours\n'
    '{} minutes\n'.format(days_workingtime, int(hours_workingtime), int(minutes_workingtime)))

# -------------------------------------------
# Using now or today
# now is better to work with timezones
# datetime.datetime.today() should return the same result as datetime.datetime.now()

# to get the today representation:
# datetime.date.today() = only today's date
# datetime.time() = datetime.time(0,0)
today = datetime.datetime.combine(datetime.date.today(), datetime.time())
print('\nRepresentation of today at midnight: ', today)

# ------------------------------------------------
# difference in seconds between two datetimes
time1 = datetime.datetime.now()
time2 = datetime.datetime(year=2020, month=1, day=1)
dif = time1 - time2
total_seconds = datetime.timedelta.total_seconds(dif)
print('\ntotal seconds between two datetimes: ', total_seconds)

# ------- REPRESENTATION AS STRINGS --------------
now = datetime.datetime.now()
now.strftime('%Y %B %d')    # Returns '2020 February 21'
now.strftime('%d/%m/%y')  # Returns '21/02/20
# documentation:
# https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior

# setting a datetime from a string:
data = datetime.datetime.strptime('05 jan 2020', '%d %b %Y')
print('05 jan 2020 = {}'.format(data))

def to_string(date):
    str_data = date.strftime('%d %B %Y')
    return str_data

def from_string(date_string, form):
    date = datetime.datetime.strptime(date_string, form)
    return date