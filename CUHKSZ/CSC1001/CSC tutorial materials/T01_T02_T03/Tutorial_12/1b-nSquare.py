from stack import ListStack

def square(n):
    SquareStack=ListStack()
    i=0
    for j in range(1,n,2):
        # print("j", j)
        for k in range(j):
            # print("k1", k)
            SquareStack.push(i)
            i+=1
        # print("before", SquareStack)
        for k in range(j-1):
            # print("k2", k)
            if not SquareStack.is_empty():
                SquareStack.pop()
        # print("after", SquareStack)
        
    while SquareStack.top()>n:
        SquareStack.pop()
    return SquareStack

print(square(100))






