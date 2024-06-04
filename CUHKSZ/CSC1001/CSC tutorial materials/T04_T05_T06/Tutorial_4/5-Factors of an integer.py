##Use try except to capture the error of not entering a number
try:
    integer=int(input("Enter an integer:"))
except:
    integer=None
    
if integer is None:
    print("The input is invalid!")
else:
    ##  Start from 2
    factor=2
    ##  Iterate from 2 to the integer
    while factor<=integer:             
        if integer%factor==0:
            ##  Stop when factor equal to the integer
            if integer==factor:         
                print(factor)
                break
            print(factor,end='')
            print()
            integer/=factor
        else:
            factor+=1
