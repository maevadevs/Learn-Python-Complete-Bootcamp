#!/usr/bin/env python
# coding: utf-8

from datetime import time

t: time = time(4, 20, 1, 999) # 4h 20m 1s 000999micros

# Let"s show the different components
print(t) # hh:mm:ss:ms.msmsms
print("hour:", t.hour)
print("minute:", t.minute)
print("second:", t.second)
print("microsecond:", t.microsecond) # 1/1000000th
print("timezone:", t.tzinfo) # timezone
print("Earliest:", time.min)
print("Latest:", time.max)
print("Resolution:", time.resolution)


from datetime import date

today: date = date.today()

print(today) # yyyy-mm-dd
print("ctime:", today.ctime())
print("tuple:", today.timetuple()) # Returns a tuple: (tm_year, tm_mon, tm_mday, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)
print("ordinal:", today.toordinal())
print("Year:", today.year)
print("Mon:", today.month)
print("Day:", today.day)
print("Earliest:", date.min)
print("Latest:", date.max)
print("Resolution:", date.resolution)


d1: date = date(2015, 3, 11)
print("d1:", d1)

d2: date = d1.replace(year=1990)
print("d2:", d2)

d3: date = d2.replace(day=26, month=12)
print("d3:", d3)


from datetime import timedelta

print(d1)
print(d2)
diff: timedelta = d1 - d2
print(diff)


from datetime import datetime, timedelta

current_date: datetime = datetime.now()
after_2yrs: datetime = current_date + timedelta(days = 730)

print("Now:", current_date)
print("After 2 years:", after_2yrs)


