class A:
    def __init__(self,newS='Welcome'):
        self.__s=newS
#        self.s2=newS

    def myprint(self):
        print(self.__s)

def main():
    a=A()
    a.myprint()
#    print(a.__s)
#    print(a.s2)

main()


    
