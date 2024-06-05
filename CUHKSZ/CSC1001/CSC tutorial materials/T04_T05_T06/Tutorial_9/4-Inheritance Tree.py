class A:
    def __init__(self,p='a'):
        self.pa=p
    def ma(self):
        print("Method ma() for A")

class B:
    def __init__(self,p='b'):
        self.pb=p
    def mb(self):
        print("Method mb() for B")

class C(A):
    def __init__(self,p='c'):
        super().__init__()
        self.pc=p
    def ma(self):
        print("Method ma() for C")
    def mc(self):
        print("Method mc() for C")

class D(C):
    def __init__(self,p='d'):
        super().__init__()
        self.pd=p
    def mc(self):
        print("Method mc() for D")
    def md(self):
        print("Method md() for D")

class E(B,D):
    def __init__(self,p='e'):
        B.__init__(self)
        D.__init__(self)
        self.pe=p
    def ma(self):
        print("Method ma() for E")
    def me(self):
        print("Method me() for E")

a,b,c,d,e=A(),B(),C(),D(),E()

##Checking what data fields and what methods each object has
for i in ['a','b','c','d','e']:
    print('-'*20)
    
    print("Data fields of %s:"%i)
    for p in ['pa','pb','pc','pd','pe']:
        try:
##          The same as trying to print(a.pa),print(a.pb),print(a.pc),print(a.pd),print(a.pe) for object a
            print(eval('%s.%s'%(i,p)))
        except:
            pass
    print("Methods of %s:"%i)
    for m in ['ma','mb','mc','md','me']:
        try:
##          The same as trying to invoke a.ma(),a.mb(),a.mc(),a.md(),a.me()for object a
            eval("%s.%s()"%(i,m))
        except:
            pass
    print('-'*20)

    


