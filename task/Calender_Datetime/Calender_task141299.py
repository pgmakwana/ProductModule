
#this package import for get the available date function
import calendar
import datetime
    
#set the first day of week
calendar.setfirstweekday(calendar.MONDAY)
##get the day of week to set from us
print("First Weekend Day:",calendar.firstweekday())
    
    
#check is leap year or not
print(calendar.isleap(int(input("Enter year to check leap year:"))))
    
    
#you get the total leap days in between two year 
print(calendar.leapdays(int(input("Enter first year to check leap day:")),int(input("Enter second year to check leap day:"))))
 
#month(_year,_month,d,i) in this function 'd' specifies the number of lines that each day will use and 'l' specifies the number of lines that each week will use
_year = int(input("Input the year : "))
_month = int(input("Input the month : "))
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(_year, _month,5,2))

 #set the weekday use setfisrdtweekday method.
calendar.setfirstweekday(calendar.SATURDAY)

#in the day_name is attribute or list to find the name of day from the number.
#second method use weekday and this method are find the weekday from the date.
print(calendar.day_name[calendar.weekday(2018, 12, 14)])
#get the weekend day number using today date
print(datetime.datetime.now().day//7)

#Get weekday of first date and last date of month. using the range function
print("First Day:",calendar.day_name[(calendar.monthrange(_year, _month))[0]],", Last Day:",calendar.day_name[calendar.weekday(_year, _month, (calendar.monthrange(_year, _month))[1])])


