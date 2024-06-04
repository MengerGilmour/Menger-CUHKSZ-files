from stack import ListStack
from Queue import ListQueue

def CheckElement(S,Q,e):
    if S.is_empty():
        print(e,'is not an element of S.')
    else:
        element=S.pop()
        Q.enqueue(element)
        if element==e:
            print(e,'is an element of S.')
        else:
            return CheckElement(S,Q,e)
  
    length=len(Q)
    for i in range(length):
        S.push(Q.dequeue())
    for i in range(length):
        Q.enqueue(S.pop())
    for i in range(length):
        S.push(Q.dequeue())
    return S

S=ListStack()
Q=ListQueue()
S.push(3)
S.push(6)
S.push(78)
S.push(9)
print('before:',S)
print('after:',CheckElement(S,Q,78))
