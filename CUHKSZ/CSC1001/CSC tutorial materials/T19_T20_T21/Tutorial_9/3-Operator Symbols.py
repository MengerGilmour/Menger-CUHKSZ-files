from math import sqrt

class Vector:
    def __init__(self,x=1,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __add__(self,v):
        Newv=Vector()
        Newv.x=self.x+v.x
        Newv.y=self.y+v.y
        return Newv
    def __sub__(self,v):
        Newv=Vector()
        Newv.x=self.x-v.x
        Newv.y=self.y-v.y
        return Newv
    def __eq__(self,v):
        return self.norm()==v.norm()
    def __gt__(self,v):
        return self.norm()>v.norm()
    def __lt__(self,v):
        return self.norm()<v.norm()    
    def norm(self):
        return sqrt(self.x**2+self.y**2)

a=Vector(2,5)
b=Vector(3,4)
print(a)
print(b)
c=a+b
print(c)
print(a.norm())
print(b.norm())
print(a==b)
print(a>b)
print(a<b)






    
        
    
    
