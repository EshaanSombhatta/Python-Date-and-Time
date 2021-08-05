#!/usr/bin/env python
# coding: utf-8

# PP: Practice Programs (Write Programs with Comments)
# PP1: Write a program to get the current date and time.
# PP2: Write a program to check whether a given year is a leap year or not.
# PP3: Display date after subtracting ‘n’ number of days from current date.
# PP4: Write a Python program to convert a string to datetime.
# Sample String : Feb 17 2020 4:37PM
#  : Expected Output : 2020-17-02 16:37:00
# 
# PP5: Calculate your age from date of birth.
# PP6: Print number of days before your next birthday.



from time import * 
from datetime.datetime.now import strftime,strptime 
from datetime import date 
from datetime.datetime import now
import calendar


#Write a program to get the current date and time.
print(ctime(time())) #time.time() provides seconds since epoch, ctime converts into a readable format

Write a program to check whether a given year is a leap year or not.
year=int(input("What's the year?"))
if year%4==0:
    if year%100!=0 or year%400==0:
        print("Year is a leap year")
    else: print("Year isn't a leap year")
else: 
    print("Year isn't a leap year")

#conditions: if a year is divisible by four, then we need to check if it's divisible by 100 or 400. 
Possibilities: 
True | False = Not a leap year
True | True = Leap year
False| True = Leap Year

Display date after subtracting ‘n’ number of days from current date.
#There are 86400 seconds in a day
days_removed=float(input("how many days do you want to go back?"))
a=time()-(86400*days_removed)
print(f"The date {days_removed} before today was {ctime(a)}")
#Basically converts all units into seconds until epoch, then subtracts x days (in seconds) then converts to readable time using ctime


#Converts formats using strptime and strftime
a=input("What is the time - please use [Month], [Date], [Year], Time in AM/PM")
b=(strptime(a,"%b %d %Y %I:%M%p"))
print(strftime("%Y-%d-%m %H:%M:%S",b))



#PP5 and 6 are one program
import calendar,time
b=input("What was your date of birth? Specify in MM/DD/YYYY format; ").split("/") #creates a list containing month, date, and year
f=time.mktime((int(b[2]), int(b[0]), int(b[1]),0, 0, 0, 0, 0, 0)) #finds the number of seconds from epoch to birth
seconds_since_birth=time.time()-f #finds seconds since birth
d=int(b[2]) #uses the year to account for leap days
leap_days=(calendar.leapdays(d,time.localtime()[0]))/(time.localtime()[0]-d) #finds the number of leapdays since birth (divided by number of years to prevent over counting in next step)
e=seconds_since_birth/(86400*(365+leap_days)) #finds average number of seconds/year and divides seconds since birth to find years/birth
print(f"You are {e} years old.") #prints years
print(f"There are {int(((e//1+1-e)*365)//1+1)} days until your next birthday") #first bit finds the amount of years until the next birthday, second bit rounds up and multiplies by 365 (not completely accurate, but stays so for a few hundred years)