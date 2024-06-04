##A function to calculate factorial of n
def factorial(n):
    result=1
    for i in range(n):
        result*=(i+1)
    return result
##Calculation of Combination(n,k)(Number of ways select k elements from n)
def Combinationnk(n,k):
    result=factorial(n)/(factorial(k)*factorial(n-k))
    return result

##Print the Yang Hui's Triangle
N=eval(input('Please input the number of lines for Young Triangle:'))
for i in range(N):
    ##    Print the spaces before printing the numbers
    print(('%-4s'*(N-i))%((' ',)*(N-i)),end='')
    ##    Print elements for the triangle, with one space between each
    for k in range(i+1):
        print('%-4d%-4s'%(Combinationnk(i,k),' '),end='')
    ##  Print the spaces on the right of each line, after the numbers
    print(('%-4s'*(N-i))%((' ',)*(N-i)))

    
        
