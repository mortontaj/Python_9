import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time is {}".format(local_time))
print("Naive UTC time is {}".format(utc_time))

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time is {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC time is {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))


# get_time = datetime.datetime(2015, 10, 25, 1, 30, 0)
# print(get_time)
# print(get_time.timestamp())
#
# s = 1445733000
# t = s + (60 * 60)
#
# gb = pytz.timezone('GB')
# dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
# dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)
#
# print("{} seconds since the epoc is {}".format(s, dt1))
# print("{} seconds since the epoc is {}".format(t, dt2))
