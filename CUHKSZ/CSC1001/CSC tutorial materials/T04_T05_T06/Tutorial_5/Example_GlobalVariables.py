a=1
b=2

## Pass the value via parameter
def Add1(a,b):
    total = a+b
    print('Sum in Add1 function is %d'%total)
    print('Within Add1 Function: a is %d, b is %d'%(a,b))
    
## Use global variable
def Add2():    
    global a, b
    total = a+b
    print('Sum in Add2 function is %d'%total)
    print('Within Add2 Function: a is %d, b is %d'%(a,b))

## Use global variables, and update their vaule within a new function
def Add3(c, d):    
    global a, b
    a=c
    b=d
    total = a+b
    print('Sum in Add3 function is %d'%total)
    print('Within Add3 Function: a is %d, b is %d'%(a,b))

def main():
    Add1(3,4)
    print('After calling Add1 function: a is %d, b is %d\n'%(a,b))
    Add2()
    print('After calling Add2 function: a is %d, b is %d\n'%(a,b))
    Add3(5,6)
    print('After calling Add3 function: a is %d, b is %d\n'%(a,b))

main()
