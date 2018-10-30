#PRERELEASE 2018 COMPUTER SCIENCE | OCTOBER/NOVEMBER
#SOLUTION TO THE TASK 1, TASK 2, AND TASK 3 RESPECTIVELY.
'''DESCRIPTION OF THE PRERELEASE:
A holiday park has a number of log cabins that it rents by te week as shown
in the table

Name                | Capacity   | Peak       |Off-peak
Hetty               |     4      |   $400.00  |  $250.00
Poppy               |     4      |   $400.00  |  $250.00
Blue Skies          |     4      |   $500.00  |  $350.00
Bay View            |     6      |   $650.00  |  $500.00
Happy Days          |     6      |   $695.00  |  $550.00
Summer Joy          |     6      |   $800.00  |  $600.00
Walkers' Rest       |     8      |   $950.00  |  $750.00
Bertie              |     8      |  $1050.00  |  $850.00
Green Forest Lodge  |    10      |  $1200.00  |  $950.00
Coppice Lodge       |    10      |  $1500.00  | $1150.00


The capacity represents the maximum number of occupants for each log cabin.
A program is needed to record and store bookings. Log cabins can only be
booked from weeks labelled on the calendar as weeks 23 to 39, inclusive.
Peak rates operate for weeks 27 to 35, inclusive, and off-peak rates apply for
weeks 23 to 26 and weeks 36 to 39, inclusive.

Required:
    Write and test a program or programs
        . Your program or programs must include appropriate prompts for the entry of data.
        . Error messages and other output need to be set out clearly and understandably.
        . All arrays, variables, constants and other identifiers must have meaningful names.'''

#TASK 1: Setting up the bookings system.
#========================================
#Write a program using Arrays to identify each log cabin, its capacity,
#cost and whether or not it has been booked for each week. identify each week
#by a number ranging from week 23 to 39. '''

'''
TASK 2: Taking a booking
========================
Extend the program to
. Identify and display which weeks are available for each log cabin and its capacity.
. Input the log cabin, number of weeks and start week for the booking
. Generate a unique booking code for the week(s) and log cabin chosen
. Store the unique booking code in your array
  (multiple week bookings will need the booking code stored multiple times.)
. Calculate and output the cost of the booking.


TASK 3: Applying a special offer.
================================
Amend the program to apply a 10% discount to any booking of three weeks or more. Output the
original cost and the discounted cost of the booking.

'''
LogCabinNames=[10]
LogCabinNames=["Hetty","Poppy","Blue Skies","Bay View","Happy Days","Summer Joy","Walkers' Rest","Bertie","Green Forest Lodge","Coppice Lodge"]

LogCabinCapacity=[10]
LogCabinCapacity=[4,4,4,6,6,6,8,8,10,10]

LogCabinPeak=[10]
LogCabinPeak=["$400.00","$400.00","$500.00","$650.00","$695.00","$800.00","$950.00","$1050.00","$1200.00","$1500.00"]

LogCabinOffpeak=[10]
LogCabinOffpeak=["$250.00","$250.00","$350.00","$500.00","$550.00","$600.00","$750.00","$850.00","$950.00","$1150.00"]

NotBooked=[10]
NotBooked=["Not Booked","Not Booked","Not Booked","Not Booked","Not Booked","Not Booked","Not Booked","Not Booked","Not Booked","Not Booked"]

Booked=[10]
Booked=["Booked","Booked","Booked","Booked","Booked","Booked","Booked","Booked","Booked","Booked"]
Weeks=[17]
Weeks=[23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
BookingStatus=[]
Bookings=[]
weekno=0
import os
import random
#from random import randint


print("Names              |Capacity  |   Peak   | Off-peak |Booked/Not Booked |")

while True:
        count=0
        for count in range(0,10):
         print('{:18}'.format(LogCabinNames[count]),"|  ",'{:2d}'.format(LogCabinCapacity[count]),"    |",'{:8}'.format(LogCabinPeak[count]),"|",'{:8}'.format(LogCabinOffpeak[count]))#,"|",'{:10}'.format(BookingStatus[0]))
        print()
        print("Total Weeks:")
        print(Weeks)
        print()
        NoOfWeeks=int(input("\n\nenter How many weeks to book?: "))
        if NoOfWeeks<=0 or NoOfWeeks >17:
         print ("Invalid No of Weeks must be 1 to 17")
        else:
         if NoOfWeeks>=1 or NoOfWeeks<=17:
          for w in range(1,NoOfWeeks+1):
           weekno=int(input("\n\nenter week no: "))
         #Off-peak Weeks
           if weekno==23: 
                 print("Off-peak Weeks",Weeks[0:4])
                 print()
                 for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    offpeakrate=int(input("enter Off-peak rate for the Log Name: "))
                    Bookings.append(offpeakrate)
           elif weekno==24: 
                  print("Off-peak Weeks",Weeks[0:4])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    offpeakrate=int(input("enter Off-peak rate for the Log Name: "))
                    Bookings.append(offpeakrate)
           elif weekno==25: 
                  print("Off-peak Weeks",Weeks[0:4])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    offpeakrate=int(input("enter Off-peak rate for the Log Name: "))
                    Bookings.append(offpeakrate)
           elif weekno==26: 
                  print("Off-peak Weeks",Weeks[0:4])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    offpeakrate=int(input("enter Off-peak rate for the Log Name: "))
                    Bookings.append(offpeakrate)
           elif weekno==36:
                  print("Off-peak Weeks",Weeks[13:17])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    offpeakrate=int(input("enter Off-peak rate for the Log Name: "))
                    Bookings.append(offpeakrate)
           elif weekno==37:
                  print("Off-peak Weeks",Weeks[13:17])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    offpeakrate=int(input("enter Off-peak rate for the Log Name: "))
                    Bookings.append(offpeakrate)
           elif weekno==38:
                  print("Off-peak Weeks",Weeks[13:17])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    offpeakrate=int(input("enter Off-peak rate for the Log Name: "))
                    Bookings.append(offpeakrate)
           elif weekno==39:
                  print("Off-peak Weeks",Weeks[13:17])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    offpeakrate=int(input("enter Off-peak rate for the Log Name: "))
                    Bookings.append(offpeakrate)
                    
#############################################################################################

           #Peak Weeks
           elif weekno==27: 
                 print("Peak Weeks",Weeks[4:13])
                 print()
                 for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    peakrate=int(input("enter peak rate for the Log Name: "))
                    Bookings.append(peakrate)
           elif weekno==28: 
                  print("Peak Weeks",Weeks[4:13])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    peakrate=int(input("enter peak rate for the Log Name: "))
                    Bookings.append(peakrate)
           elif weekno==29: 
                  print("Peak Weeks",Weeks[4:13])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    peakrate=int(input("enter peak rate for the Log Name: "))
                    Bookings.append(peakrate)
           elif weekno==30: 
                  print("Peak Weeks",Weeks[4:13])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    peakrate=int(input("enter peak rate for the Log Name: "))
                    Bookings.append(peakrate)
           elif weekno==31:
                  print("Peak Weeks",Weeks[4:13])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    peakrate=int(input("enter peak rate for the Log Name: "))
                    Bookings.append(peakrate)
           elif weekno==32:
                  print("Peak Weeks",Weeks[4:13])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    peakrate=int(input("enter peak rate for the Log Name: "))
                    Bookings.append(peakrate)
           elif weekno==33:
                  print("Peak Weeks",Weeks[4:13])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    peakrate=int(input("enter peak rate for the Log Name: "))
                    Bookings.append(peakrate)
           elif weekno==34:
                  print("Peak Weeks",Weeks[4:13])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    peakrate=int(input("enter peak rate for the Log Name: "))
                    Bookings.append(peakrate)
           elif weekno==35:
                  print("Peak Weeks",Weeks[4:13])
                  print()
                  for x in range(1):
                    bookingno=int(random.randint(11,11)*weekno,)
                    print("Your Booking Code is: ",bookingno)
                    Bookings.append(bookingno)
                    LogName=str(input("enter Log Name: "))
                    Bookings.append(LogName)
                    capacity=int(input("enter Capacity: "))
                    Bookings.append(capacity)
                    peakrate=int(input("enter peak rate for the Log Name: "))
                    Bookings.append(peakrate)         
           else:
              print("Peak Off Week/s",Weeks[0:4],"<|>",Weeks[13:17])
              print("Peak-Week/s: >",Weeks[4:13],"\n")
   
