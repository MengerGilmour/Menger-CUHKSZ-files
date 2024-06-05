#Define a function to check whether the values of three sides is valid
def isValid(side1,side2,side3):
    return (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1)

#Calculate the area of a triangle given the values of its three sides
def area(side1,side2,side3):
    costheta=(side1**2+side2**2-side3**2)/(2*side1*side2)
    sintheta=(1-costheta**2)**0.5
    return 0.5*side1*side2*sintheta

