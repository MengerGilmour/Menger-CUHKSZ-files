####①
##class A:
##    def __new__(self):
##        print("A's __new__() invoked")
##
##    def __init__(self):
##        print("A's __init__() invoked")
##
##class B(A):
##    def __new__(self):
##        print("B's __new__() invoked")
##
##    def __init__(self):
##        print("B's __init__() invoked")
##
##def main():
##    b=B()
##    a=A()
##
##main()

####②
##class A:
##    def __new__(self):
##        self.__init__(self)
##        print("A's __new__() invoked")
##
##    def __init__(self):
##        print("A's __init__() invoked")
##
##class B(A):
##    def __new__(self):
##        self.__init__(self)
##        print("B's __new__() invoked")
##
##    def __init__(self):
##        print("B's __init__() invoked")
##
##def main():
##    b=B()
##    a=A()
##
##main()
##
##③
class A:
    def __new__(self):
        self.__init__(self)
        print("A's __new__() invoked")

    def __init__(self):
        print("A's __init__() invoked")

class B(A):
    def __init__(self):
        print("B's __init__() invoked")

def main():
    b=B()
    a=A()

main()


