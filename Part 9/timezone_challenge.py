# create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list
#
# The program will then display the time in that timezone,
# as well as local time and UTC time.
#
# Entering 0 as a choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time..
import pytz
import datetime

number = {1: {"1": "US/Eastern"},
          2: {"2": "US/Central"},
          3: {"3": "US/Mountain"},
          4: {"4": "US/Pacific"},
          5: {"5": "US/Alaska"},
          6: {"6": "US/Arizona"},
          7: {"7": "US/Hawaii"},
          8: {"8": "US/Michigan"},
          9: {"9": "US/Indiana-Starke"},
          10: {"10": "US/East-Indiana"},
          }


while True:
    for val in number.values():
        print(val)
    removed_symbols = "[", "]", "'"
    time_zone = ""
    chose = int(input("Enter a number between 1 and 10 or 0 to quit: "))
    zone = number.get(chose)

    if chose == 0:
        print("Bye!")
        break

    else:
        for char in zone.values():
            if char == removed_symbols:
                continue

            else:
                time_zone = "".join(char)

        chosen = pytz.timezone(time_zone)
        print("*" * 60)
        print()
        print("{}: \t{}".format(chosen, datetime.datetime.now(tz=chosen).strftime("%A %x %X %z")))
        print("Local time: \t{}".format(datetime.datetime.now().strftime("%A %x %X %z")))
        print("UTC time: \t\t{}".format((datetime.datetime.utcnow().strftime("%A %x %X %z"))))
