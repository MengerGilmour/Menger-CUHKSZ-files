from SLList import SLList

def link(L,M):
    Lp=SLList()
    Lp.head=L.head
    L.tail.pointer=M.head
    Lp.tail=M.tail
    Lp.size=L.size+M.size
    return Lp

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
link(L,M).iterate()
