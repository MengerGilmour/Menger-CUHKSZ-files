from MyTriangle import *        #Import all functions in the module MyTriangle

#Define a main function to input three sides of a triangle and judge whether it is a valid triangle
def main():
    a,b,c=eval(input("Enter the three sides of a triangle:"))
    if isValid(a,b,c):
        print("The area of the triangle is %.2f."%area(a,b,c))
    else:
        print("The input is invalid.")

main()



