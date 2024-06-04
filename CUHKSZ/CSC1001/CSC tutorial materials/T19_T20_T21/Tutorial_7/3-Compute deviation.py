def mean(x):
    return sum(x)/len(x)

def deviation(x):
    deviationList=[(xi-mean(x))**2/(len(x)-1) for xi in x]
    deviation=sum(deviationList)**0.5
    return deviation

def main():
    numberLine=input("Enter numbers whose mean and deviation you want to calculate(separated by space):\n")
    numberList=numberLine.split()
##  A quick way to change a list [x1,x2,x3,...] to a new list
##  [f(x1),f(x2),f(x3),...] where f is some function or mapping.
    numberList=[eval(x) for x in numberList]
    print("The mean is",mean(numberList))
    print("The standard deviation is",deviation(numberList))

main()
