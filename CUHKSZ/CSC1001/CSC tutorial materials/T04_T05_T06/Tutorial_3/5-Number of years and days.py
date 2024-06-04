## Prompt the user to enter the minutes
minute=eval(input("Enter the number of minutes:"))

##Use the operator to find the years and days
##The number of hours
hour=minute//60
## The number of days
day=hour//24
## The number of years
year=day//365
##The number of days left
day%=365

##Display the result
print("That minutes will equal to",year,"years and",day,"days.")
