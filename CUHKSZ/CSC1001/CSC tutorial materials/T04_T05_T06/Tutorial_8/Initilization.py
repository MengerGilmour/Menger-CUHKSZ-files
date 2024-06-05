class A:
    def __init__(self, i=0, j=0, k=0):
        self.i=i
        self.j=j
        self.k=k

class D:
    def __init__(self, i):
        self.i=i

def main():
    a=A()
    b=A(1,2)
    c=A(1,2,3)
    print('a: i is %d, j is %d, k is %d'%(a.i, a.j, a.k))
    print('b: i is %d, j is %d, k is %d'%(b.i, b.j, b.k))
    print('c: i is %d, j is %d, k is %d'%(c.i, c.j, c.k))

    #d=D()
    d=D(1)
    print('d: i is %d'%d.i)

main()
    
