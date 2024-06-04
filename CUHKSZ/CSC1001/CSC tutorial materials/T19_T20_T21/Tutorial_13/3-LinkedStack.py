class Node:
    
    def __init__(self,e,node):
        self.element=e
        self.pointer=node

class LinkedStack:
    
    def __init__(self):
        self.head=None
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def top(self):
        if self.is_empty():
            print('Stack is empty.')
        else:
            return self.head.element

    def pop(self):
        if self.is_empty():
            print('Stack is empty.')
        else:
            answer=self.head.element
            self.head=self.head.pointer
            self.size-=1
            return answer

    def push(self,e):
        self.head=Node(e,self.head)
        self.size+=1

    def __str__(self):
        stack=[]
        node=self.head
        while node != None:
            stack.append(node.element)
            node=node.pointer
        stack.reverse()
        return str(stack)


s=LinkedStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s)
print(s.top())


##class Node:
##    
##    def __init__(self,e,node):
##        self.element=e
##        self.pointer=node
##
##class LinkedStack:
##    
##    def __init__(self):
##        self.head=None
##        self.size=0
##
##    def __len__(self):
##        return self.size
##
##    def is_empty(self):
##        return self.size==0
##
##    def top(self):
##        if self.is_empty():
##            print('Stack is empty.')
##        else:
##            #①
##
##    def pop(self):
##        if self.is_empty():
##            print('Stack is empty.')
##        else:
##            #②
##
##    def push(self,e):
##        #③
##
##    def __str__(self):
##        #④



        
