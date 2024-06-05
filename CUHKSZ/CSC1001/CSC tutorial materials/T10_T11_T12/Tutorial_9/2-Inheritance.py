class A:
    def __init__(self,i=0,j=0):
        self.__i=i
        self.j=j
    def __m1(self):
        self.__i+=1
    def m2(self):
        return self.__i
    
class B(A):
    def __init__(self,i=1,j=1):
        super().__init__(i,j)

b=B()
##print(b.__i)    #①
print(b.j)      #②
##print(b.__m1()) #③
print(b.m2())   #④






