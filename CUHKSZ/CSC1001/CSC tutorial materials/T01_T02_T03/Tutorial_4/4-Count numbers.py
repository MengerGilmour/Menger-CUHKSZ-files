##Give an initial value other than 0
integer=None
##To count positive numbers
countPositive=0
##To count negative numbers
countNegative=0
##To count total numbers
count=0
##To sum up the numbers
sumOfNum=0

##if integer==0, stop the loop
while integer != 0:       
    ##  Use try except to capture the error input 
    try:
        integer=int(input("Enter an integer, the input ends if it is 0:"))
    except:
        print("Invalid number!Please input again!")
        ##  Continue the loop while not execute the following code
        continue
    
    if integer>0:
        countPositive+=1
    elif integer<0:
        countNegative+=1
    else:
        ##  Continue without executing the following code, in this case integer=0, will break the loop
        continue
    
    count+=1
    sumOfNum+=integer
    
if count==0:
    print("No numbers are input except 0")
else:
    print("The number of positives is %d"%countPositive)
    print("The number of negative is %d"%countNegative)
    print("The sum of numbers is %d"%sumOfNum)
    print("The average of numbers is %.2f"%(sumOfNum/count))
