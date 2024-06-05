from DLList import DLList

def LinkedInsertionSort(l):
    i=l.header.nxt.nxt
    while i != l.trailer:
        j=i.prev
        buf=i.element
        while j != l.header and j.element>buf:
            j.nxt.element=j.element
            j=j.prev
        j.nxt.element=buf
        i=i.nxt
    return l

L=DLList()
L.insert_between(1,L.header,L.trailer)
L.insert_between(2,L.header,L.header.nxt)
L.insert_between(4,L.header,L.header.nxt)
L.insert_between(6,L.header,L.header.nxt)
L.insert_between(5,L.header,L.header.nxt)
L.insert_between(9,L.header,L.header.nxt)
L.insert_between(8,L.header,L.header.nxt)
L.insert_between(7,L.header,L.header.nxt)
L.iterate()
LinkedInsertionSort(L).iterate()
