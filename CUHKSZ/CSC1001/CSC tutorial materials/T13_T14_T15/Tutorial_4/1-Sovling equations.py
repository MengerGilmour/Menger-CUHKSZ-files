##Prompt the users to input the coefficients
a,b,c=eval(input("Enter coefficients a,b and c in the equation ax^2+bx+c=0:"))

##Calculate the discriminant
discriminant=b**2-4*a*c

##Obtain the roots based on different conditions for the discriminant
if discriminant>0:
    x1=(-b+discriminant**0.5)/2/a
    x2=(-b-discriminant**0.5)/2/a
    print('The two roots of the equation are x1=%.2f and x2=%.2f.'%(x1,x2))
elif discriminant==0:
    x=-b/2/a
    print("There is only one root x=%.2f."%x)
else:
    print("The equation has no real roots.")
