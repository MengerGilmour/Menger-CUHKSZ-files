from Circle import Circle

def printAreas(c,times):
    print(('%-6s'*5)%('n',' ','Radius',' ','Area'))
    while times>=1:
        c.radius=c.radius+1
        times=times-1
        print('%-6d%-6s%-6d%-6s%-6.2f'%(times,' ',c.radius,' ',c.getArea()))

def main():
    myCircle=Circle()
    n=5
    print("Before invoking the function:")
    print('Radius of myCircle is',myCircle.radius)
    print('n is',n)
    print('-----------------------------')
    printAreas(myCircle,n)
    print('-----------------------------')
    print('After invoking the function:')
    print('Radius of myCircle is',myCircle.radius)
    print('n is',n)

main()


##from Circle import Circle
##
##def printAreas(c,times):
##    while times>=1:
##        c.radius=c.radius+1
##        times=times-1
##        print(times,c.radius,c.getArea())
##        
##def main():
##    myCircle=Circle()
##    n=5
##    printAreas(myCircle,n)
##    print(myCircle.radius)
##    print(n)
##
##main()





