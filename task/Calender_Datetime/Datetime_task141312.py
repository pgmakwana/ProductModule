
from datetime import date
from datetime import time
import datetime
from datetime import timedelta
from datetime import tzinfo
import pytz
from datetime import timezone
import calendar


#Addition of 2 Date times.
first_date = timedelta(days=1850, hours=13, minutes=20, seconds=60, microseconds=253)
#using timedelta class set the date and time and create own date
second_date=timedelta(days=652, hours=22, minutes=18, seconds=42, microseconds=35)
#addition of two date
print("Addition Of Two Date: ",second_date + first_date)


#Difference of 2 Date times.
print("Differance Of Two Date: ",first_date - second_date)


#Multiplication of time with integer & Float.
print("Multiplication of time: ",timedelta(seconds=(int(first_date.seconds * second_date.seconds))))

#Division of time with integer & Float.
print("Division of time: ",timedelta(seconds=(int(second_date.seconds  //  first_date.seconds))))



#Difference of 2 date time.quotient and the remainder
print("Difference of 2 date days:",divmod(first_date.days, second_date.days))
print("Difference of 2 date month:",divmod(first_date.days/30, second_date.days/30))
print("Difference of 2 time seconds:",divmod(first_date.seconds, second_date.seconds))
print("Difference of 2 time minute:",divmod(first_date.min, second_date.min))
#print("Difference of 2 time hours:",divmod((first_date.days//30//24), (second_date.min//30/24)))


#Get Current month, current date, current week day, current year, and add hours, minutes, days, month and years in it.
print("\nCurrent Month: ",datetime.datetime.today().strftime("%B"))
print("Current Year: ",datetime.datetime.today().strftime("%Y"))
print("Current Week Day: ",datetime.datetime.today().strftime("%A"))
print("Current Day: ",datetime.datetime.today().strftime("%D"))
print("Current hrs: ",datetime.datetime.today().strftime("%H"))

print("\n\nCurrent Month: ",int(datetime.datetime.today().strftime("%m"))+2)
print("Current Year: ",int(datetime.datetime.today().strftime("%Y"))+1)
print("Current Day: ",int(datetime.datetime.today().strftime("%d"))+10)
print("Current hrs: ",int(datetime.datetime.today().strftime("%H"))+4)


#Get local timezone and current  UTC time. and Convert it in local timezone. also convert it in other timezone.
print("\nCurrent UTC timezone",datetime.datetime.utcnow())
print("add local timezone in utc timezone: ",pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None).astimezone())


#Convert time to string and string to time.
datetime_object=datetime.datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
print("\n",datetime_object)
print(str(datetime_object))


_time = datetime.datetime.strptime('01:30','%H:%M').time()
_datetime = datetime.datetime.combine(datetime.date.today(), _time)
print("\nCombine Datetime: ",_datetime)

#Get Current month name from date
print("\nCurrent Month Name:",datetime.datetime.today().strftime("%B"))

#Get time in 12-hour clock & 24-hour clock
print("\ntime in 12-hour clock: ",datetime.datetime.today().strftime("%I"))
print("time in 24-hour clock: ",datetime.datetime.today().strftime("%H"))

#Get Datetime with century number and without century number. ie. 2018 & 18.
print("\nDatetime with century number :",datetime.datetime.today().strftime("%Y"))
print("Datetime without century number :",datetime.datetime.today().strftime("%y"))

#Get Locale’s equivalent of either AM or PM. from Date.
print("\nAM or PM: ",datetime.datetime.today().strftime("%p"))

#Get Day of year from date time. (01,...366)
print("\nDay of year: ",datetime.datetime.now().timetuple().tm_yday)


#Get Week number of year by both (Sunday as First Day of week & Monday as First Day of week).
print("\nWeek Number Of Year: ",datetime.datetime.today().isocalendar()[1])


#Get Current Date and Print it in various format like DD/MM/YY, YY/MM/DD, MM-DD-YY, DD-MM-YY, YY-DD-MM
today_date=datetime.datetime.today()

print("\nprint Date In different different format\n",today_date)
print(today_date.strftime("%b %d %Y %H:%M:%S"))
print(today_date.strftime("%B %d %Y %H:%M:%S"))
print(today_date.strftime("%d %m %Y %H:%M:%S"))
print(today_date.strftime("%b %d %y"))
print(today_date.strftime("%m %d %y %H:%M"))


