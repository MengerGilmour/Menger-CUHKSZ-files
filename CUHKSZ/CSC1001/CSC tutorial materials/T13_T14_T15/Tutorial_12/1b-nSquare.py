from stack import ListStack

def square(n):
    SquareStack=ListStack()
    i=0
    for j in range(1,n,2):
        for k in range(j):
            SquareStack.push(i)
            i+=1
        for k in range(j-1):
            if not SquareStack.is_empty():
                SquareStack.pop()
    while SquareStack.top()>n:
        SquareStack.pop()
    return SquareStack

print(square(100))






