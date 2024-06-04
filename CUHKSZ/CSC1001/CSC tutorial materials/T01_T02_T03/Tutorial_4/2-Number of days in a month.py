##Prompt the user to enter the month and year
month,year=eval(input("Enter the month and year:"))

##Use multi-way decision flow to handle different cases for different month
if month==1:
##  Use numOfDay to store the number of days    
    numOfDay=31                                                                             
    print("January %d has %d days"%(year,numOfDay))      
elif month==2:
    ##  Conditions for leap year(闰年)
    if (year%4==0 and year%100 != 0) or year%400==0:    
        numOfDay=29
        print("February %d has %d days"%(year,numOfDay))
    else:
        numOfDay=28
        print("February %d has %d days"%(year,numOfDay))
elif month==3:
    numOfDay=31
    print("March %d has %d days"%(year,numOfDay))
elif month==4:
    numOfDay=30
    print("April %d has %d days"%(year,numOfDay))
elif month==5:
    numOfDay=31
    print("May %d has %d days"%(year,numOfDay))
elif month==6:
    numOfDay=30
    print("June %d has %d days"%(year,numOfDay))
elif month==7:
    numOfDay=31
    print("July %d has %d days"%(year,numOfDay))
elif month==8:
    numOfDay=31
    print("August %d has %d days"%(year,numOfDay))
elif month==9:
    numOfDay=30
    print("September %d has %d days"%(year,numOfDay))
elif month==10:
    numOfDay=31
    print("October %d has %d days"%(year,numOfDay))
elif month==11:
    numOfDay=30
    print("November %d has %d days"%(year,numOfDay))
else:
    numOfDay=31
    print("December %d has %d days"%(year,numOfDay))
