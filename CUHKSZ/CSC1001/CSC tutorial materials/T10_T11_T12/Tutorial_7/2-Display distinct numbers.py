numberLine=input("Enter ten numbers(separated by space):\n")
numberList=numberLine.split()
distinctnumber=[]
for number in numberList:
    if number not in distinctnumber:
        distinctnumber.append(number)
print("The distinct numbers are:",end='')
for number in distinctnumber:
    print(number,end=' ')
