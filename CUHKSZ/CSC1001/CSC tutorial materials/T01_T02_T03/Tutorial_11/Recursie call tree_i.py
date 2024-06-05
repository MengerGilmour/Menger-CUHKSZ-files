def main():
    y=foo(3)
    #y=foo(4)
    bar(2)
    print('y is ',y)

def foo(x):
    if x%2!=0:
        return 0
    else:
        return x+foo(x-1)

def bar(n):
    if n>0:
        print(n)
        bar(n-1)

main()
