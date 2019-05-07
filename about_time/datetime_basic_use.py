"""
created by nzh
Date: 2019/3/21 4:59 PM
"""
from datetime import datetime, tzinfo, timezone, timedelta
import time


# datetime.today()
# dt1 = datetime.today()
# print(dt1, type(dt1))
#
# dt2 = datetime.fromtimestamp(time.time())
# print(dt2, type(dt2))


# datetime.now()
# dt3 = datetime.now()
# print(dt3, type(dt3))


# datetime.utcnow()
# dt4 = datetime.utcnow()
# print(dt4, type(dt4))


# 构造tzinfo
tz_utc_8 = timezone(timedelta(hours=8))

timestamp = time.time()
# datetime_from_timestamp = datetime.fromtimestamp(timestamp)
# print(datetime_from_timestamp, type(datetime_from_timestamp))


# dt5 = datetime.utcfromtimestamp(timestamp)
# print(dt5, type(dt5))


# date_string = "2019-08-30 16:00:00"
# date_format = "%Y-%m-%d %H:%M:%S"
# struct_time = time.strptime(date_string, date_format)
# dt6 = datetime(*struct_time)
# print(dt6, type(dt6))


def timestamp_to_UTC(timestamp):
    time.struct_time()