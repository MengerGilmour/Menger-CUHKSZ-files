integerLine=input("Enter several integers in the interval [1,9](separated by space):\n")
integerList=integerLine.split()
countDict=dict()
for integer in integerList:
    countDict[integer]=countDict.get(integer,0)+1
for key,value in countDict.items():
    if value>1:
        print("%s occurs %d times."%(key,value))
    else:
        print("%s occurs %d time."%(key,value))
