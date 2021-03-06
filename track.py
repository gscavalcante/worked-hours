import re
import os
import sys
import csv
import argparse
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M"
FIELD_NAMES = ["date", "start", "end"]
file_name = ""

def init():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    global file_name
    file_name = dir_path + "/worked_hours.csv"

    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--time",
        dest="hour",
        help="Value to change de hour manually")

    args = parser.parse_args()
    add_time(args.hour)

def add_time(hour):
    today = datetime.now()

    if hour and hour.split():
        validate_hour(hour)
    else:
        hour = today.strftime(TIME_FORMAT)

    date = get_last_date()
    if date is None:
        date = today.strftime(DATE_FORMAT)
        check_in(hour, date)
    else:
        check_out(hour)

def validate_hour(hour):
    pattern = re.compile("^([0-2][0-9]:[0-5][0-9])$")
    if bool(pattern.match(hour)) == False:
        print("The input {} is not a valid hour".format(hour))
        sys.exit(1)

def create_csv_file():
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)

        writer.writeheader()

def get_last_date():
    try:
        with open(file_name, "r") as csvfile:
            lines = csvfile.readlines()

            if not lines:
                return None

            last_line = lines[-1]
            date,start,end = last_line.split(",")

            if not end.strip():
                return date
            
            return None
    except FileNotFoundError:
        create_csv_file()
        return None

def check_out(hour):
    r = csv.reader(open(file_name))
    lines = list(r)
    lines[-1][2] = hour
    
    writer = csv.writer(open(file_name, "w"))
    writer.writerows(lines)

    print("Check-out done with success at", hour)

def check_in(hour, date):
    with open(file_name, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)

        writer.writerow({"date": date, "start": hour})
        print("Check-in done with success at", hour)

if __name__ == "__main__":
    init()