def PrintDigit(n):
    if n//10==0:
        print(n)
    else:
        PrintDigit(n//10)
        print(n%10)

PrintDigit(3125)
        

