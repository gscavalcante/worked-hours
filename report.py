import os
import csv
import argparse
from datetime import datetime, timedelta

file_name = ""
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M"

def init():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    global file_name
    file_name = dir_path + "/worked_hours.csv"

    parser = argparse.ArgumentParser(
        description="Get the data processed to be easier to understand"
    )

    parser.add_argument("-d", "--date",
        help="Date to check the information"
    )
    parser.add_argument("--detailed",
        help="Show the lines used to calculate the amount",
        action="store_true"
    )
    parser.add_argument("-t", "--today",
        help="Show the amount of hours at the current day",
        action="store_true"
    )
    parser.add_argument("-y", "--yesterday",
        help="Show the amount of hours at the last day",
        action="store_true"
    )

    args = parser.parse_args()
    date = parse_date(args)
    
    check_day(date, args.detailed)

def parse_date(args):
    date = None

    if args.date:
        date = args.date
    elif args.yesterday:
        yesterday_date = datetime.now() - timedelta(1)
        date = yesterday_date.strftime(DATE_FORMAT)
    else:
        today_date = datetime.now()
        date = today_date.strftime(DATE_FORMAT)

    return date

def time_to_decimal(time):
    hour, minute, second = str(time).split(":")

    minute = ((float(minute) * 10) / 6) / 100

    return round(float(hour) + minute, 2)

def check_day(day, detailed):
    total = .0

    with open(file_name, "r", newline="") as worked_hours:
        reader = csv.reader(worked_hours)

        for row in reader:
            if len(row) == 3 and len(row[2]) == 5 and day == row[0]:
                start_time = datetime.strptime(row[1], TIME_FORMAT)
                end_time = datetime.strptime(row[2], TIME_FORMAT)

                total += time_to_decimal(end_time - start_time)

                if detailed:
                    print(row)

    if total is .0:
        print("There isn\'t any checkout on the day {}. \
            \nYou need to finish your work hour before check the amount.".
            format(day))
    else:
        print(total)

init()
