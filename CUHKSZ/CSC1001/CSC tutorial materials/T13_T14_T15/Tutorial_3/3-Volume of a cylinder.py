##From the math module import the variable pi=π
from math import pi

##Prompt up the indicator for users to enter radius and length
radius=eval(input("Enter radius of the cylinder:"))
length=eval(input("Enter length of the cylinder:"))

##Manipulate the variables with operators to find the result
area=radius*radius*pi
volume=area*length

##Display the result,%.2f means keeping two digits after decimal point
print("The area is:%.2f"%area)
print("The volume is:%.2f"%volume)


