class Count:
    def __init__(self,count=0):
        self.count=count

def m(c,n):
    c=Count(5)
    n=3

def main():
    c=Count()
    n=1
    m(c,n)

    print('count is',c.count)
    print('n is',n)

main()



