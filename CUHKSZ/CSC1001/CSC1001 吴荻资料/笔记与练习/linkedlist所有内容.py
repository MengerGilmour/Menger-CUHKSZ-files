class Node:
    def __init__(self,element,pointer): #定义两个parameter，一个是元素值，一个是下一项的指示
        self.element=element
        self.pointer=pointer
#用单链表打印堆栈stack
class linked_stack:
    def __init__(self):
        self.head=None
        self.size=0
    def len(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def push(self,e):#简短表达即可
        self.head=Node(e,self.head) #不要忘记pointer的值是self.head
        self.size+=1
    def pop(self):
        if self.is_empty():
            print('the stack is empty')
        else:#这里不用考虑是否为空的问题了
            answer=self.head
            self.head=self.head.pointer #不是self.head.pointer=self.head,注意赋值是右边给左边，要理解什么意思！
            self.size-=1
            return answer.element
    def top(self):
        if self.is_empty():
            print('stack is empty')
        else:
            return self.head.element
    def __str__(self):
        stack=[]
        pointer=self.head
        while pointer!=None:
            stack.append(pointer.element)
            pointer=pointer.pointer
        stack.reverse()#注意stack是倒序的，要把他还原回顺序表示
        return str(stack)
#用单链表打印队列queue：比stack特殊的是要考虑tail
class linked_queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def len(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def first(self):
        if self.is_empty():
            print('queue is empty')
        else:
            return self.head.element
    def dequeue(self):
        if self.is_empty:
            print('queue is empty')
        else:
            answer=self.head
            self.head=self.head.pointer
            self.size-=1
            if self.is_empty(): #考虑tail！！这里比stack多了一步
                self.tail=None
        return answer.element
    def enqueue(self,e):
        newest=Node(e,None)#和stack的push类比，那个是newest=Node(e,self.head)，不过是pointer不一样而已
        # newest.pointer=None
        if self.is_empty():#两种情况，queue空与非空，要分开讨论；与stack不同
            self.head=newest
        else: #注意是if，else结构
            self.tail.pointer=newest #把newest赋值给指针
        self.tail=newest
        self.size+=1
    def __str__(self):
        queue=[]
        pointer=self.head
        while pointer!=None:
            queue.append(str(pointer.element))
            pointer=pointer.pointer
        return str(queue)

#a queue with circularly linked list
class Node:
    def __init__(self,element,pointer):
        self.element=element
        self.pointer=pointer
class CQueue:
    def __init__(self):
        self.__tail=None
        self.__size=0
    def len(self):
        return self.__size
    def is_empty(self):
        return self.__size==0
    def first(self):
        if self.is_empty():
            print('queue is empty')
        else:
            head=self.__tail.pointer #注意，这里不是单链表的直接return self.head.element,循环链表没有self.head
            return head.element
    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            answer=self.__tail.pointer #oldhead=self.__tail.pointer
            self.size-=1
            if self.is_empty():
                self.__tail=None
            else:
                self.__tail.pointer=self.__tail.pointer.pointer #oldhead.pointer\answer.pointer
            return answer.element
    def enqueue(self):
        newest=Node(e,None) #仍然要设置newest指向None
        if self.is_empty():
            newest.pointer=newest #给指针赋值，应该这样写而不是调过来写！！！
        else:
            newest.pointer=self.__tail.pointer
            self.__tail.pointer=newest
        self.__tail=newest
        self.size+=1
#双链表：注意header,trailer
class Node:
    def __init__(self,element,prev,nxt): #定义前项和后项
        self.element=element
        self.prev=prev
        self.nxt=nxt
class DLList:
    def __init__(self):
        self.header=Node(None,None,None) #关键：创建header和trailer，as gummy/sentinel
        self.trailer=Node(None,None,None)
        self.header.nxt=self.trailer
        self.trailer.prev=self.header
        self.size=0
    def len(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def insert_between(self,e,predecessor,successor):
        newest=Node(e,predecessor,successor)
        predecessor.nxt=newest
        successor.prev=newest
        self.size+=1
        return newest
    def delete_node(self,node):
        predecessor=node.prev
        successor=node.nxt
        predecessor.nxt=successor
        successor.prev=predecessor
        self.size-=1
        element=node.element #用element来储存node.element
        node.prev=node.nxt=node.element=None #这一步的意思是，此时node变成了（None，None，None）
        return element
    def iterate(self):
        pointer=self.header.nxt #初始，pointer为有元素的第一项
        print('the elements in the list:')
        while pointer.nxt!=self.trailer: #用一个while循环遍历，直到下一项成为trailer
            print(pointer.element)
            pointer=pointer.nxt
#bubble sort
def bubblesort(list):
    listlength=len(list) #初始长度为列表的长度
    while listlength>0:
        for i in range(listlength):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
        listlength-=1 #重新进入while循环-for循环
        return list
#bubble sort over a singly linked list
def linkedbubblesort(q):
    listlength=q.size
    while listlength>0:
        index=0
        pointer=q.head
        while index<listlength:
            if pointer.element>pointer.pointer.element:
                pointer.element,pointer.pointer.element=pointer.pointer.element,pointer.element
            index+=1
            pointer=pointer.pointer
        listlength-=1
    return q
def output(q):
    pointer=q.head
    while pointer:
        print(pointer.element)
        pointer=pointer.pointer
#quick sort over a standard list
def quicksort(list,low,high):
    i=low
    j=high
    if i>=j:
        return L
    key=list[i]
    if i<j:
        while i<j and list[j]>key:
            j-=1
        list[i]=list[j]
        while i<j and list[j]<key:
            j+=1
        list[j]=list[i]
    list[i]=key
    quicksort(list,low,i-1)
    quicksort(list,j+1,high)
    return list
#quick sort over a singly linked list
from LinkedQueue import LinkedQueue
def LQS(q,head,tail):
    i=j=q.head.pointer #i和j都指向head的下一项
    pivot=q.head.element #规定pivot为head项的element值
    x=i.pre
    x.pointer=i #为了表示i的前一项，设一个x来指代
    if True: #可以设一个列表来模拟，理解原理
        while j.element<pivot and j!=q.tail:
            i.element,j.element=j.element,i.element # 交换i和j的值
            i=i.pointer #i和j都向右手边移动一个值
        while j.element>pivot and j!=q.tail:
            j=j.pointer #只有j向右手边移动
    pivot,x.element=x.element,pivot #改变pivot的值，交换位置
    LQS(q,head,x) #利用递归
    LQS(q,i,tail)
    return q
LQS(linkedlist,linkedlist.head,linkedlist.tail)

#linked listTUT
#1 连接两个单链表
from SLList import SLList
def link(L,M):
    Lp=SLList()
    Lp.head=L.head
    Lp.tail.pointer=M.head
    Lp.tail=M.tail
    Lp.size=L.size+M.size #容易遗漏的一步，注意size也会改变
    return Lp
#检验程序的运行
L=SLList()
L.insert_head(10)
L.insert_tail(20)
L.insert_tail(30)

M=SLList()
M.insert_head(60)
M.insert_head(50)
M.insert_head(40)

L.iterate()
M.iterate()
Link(L,M).iterate()

#2.手写程序练习













































