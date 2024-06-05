#What are problems of the following program?
##class A:
##    def __init__(self):
##        self.__i=i
##
##def main():
##    a=A(5)
##    print(a.__i)
##
##main()

#Reference Answer (1) :Change to public and initialize data file i when constructing the object
class A:
    def __init__(self,i):
        self.i=i

def main():
    a=A(5)
    print(a.i)

main()


#Reference Answer (2): Change to public and intialize data file i when invoking __init__. This is not a good method for data field initilization.
class A:
    def __init__(self):
        self.i=5

def main():
    a=A()
    print(a.i)

main()

#Reference Answer (3): Use a getter
class A:
    def __init__(self,i):
        self.__i=i
    def geti(self):
        return self.__i

def main():
    a=A(5)
    print(a.geti())

main()
