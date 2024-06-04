def PrintDigit(n):
    if n//10==0:
        print(n)
    else:
        print(n%10)
        PrintDigit(n//10)

PrintDigit(3125)
