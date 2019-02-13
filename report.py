import csv
import sys
from datetime import datetime, timedelta

FILE_NAME = "worked_hours.csv"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M"

def time_to_decimal(time):
    hour, minute, second = str(time).split(":")

    minute = ((float(minute) * 10) / 6) / 100

    return round(float(hour) + minute, 2)

def check_day(day):
    total = .0

    with open(FILE_NAME, 'rb') as worked_hours:
        csv_reader = csv.reader(worked_hours)
        next(csv_reader) # Jump the header

        for row in csv_reader:
            if len(row) == 3 and len(row[2]) == 5 and day == row[0]:
                start_time = datetime.strptime(row[1], TIME_FORMAT)
                end_time = datetime.strptime(row[2], TIME_FORMAT)

                total += time_to_decimal(end_time - start_time)
    if total == .0:
        print 'There isn\'t any checkout on this day. ' \
            'You need to finish your work hour before check the ammount.'
    else:
        print total

def init():
    option = sys.argv[1]

    if option == '-d' or option == '--date':
        check_day(sys.argv[2])
    elif option == 'today':
        today_date = datetime.now()
        check_day(today_date.strftime(DATE_FORMAT))
    elif option == 'yesterday':
        yesterday_date = datetime.now() - timedelta(1)
        check_day(yesterday_date.strftime(DATE_FORMAT))
    else:
        print 'Error: Unknown option %s' % option
        exit(1)

init()
