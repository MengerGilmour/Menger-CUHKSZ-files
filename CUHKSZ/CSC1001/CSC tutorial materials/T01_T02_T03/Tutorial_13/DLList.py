class Node:
    def __init__(self,element,prev,nxt):
        self.element = element
        self.prev = prev
        self.nxt = nxt

class DLList:
    def __init__(self):
        self.header = Node(None,None,None)
        self.trailer = Node(None,None,None)
        self.header.nxt = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self,e,predecessor,successor):
        newest = Node(e,predecessor,successor)
        predecessor.nxt = newest
        successor.prev = newest
        self.size += 1
        return newest

    def delete_node(self,node):
        predecessor = node.prev
        successor = node.nxt
        predecessor.nxt = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element
        node.prev = node.nxt = node.element = None
        return element

    def iterate(self):
        pointer = self.header.nxt
        print('The element in the list: ')
        while pointer != self.trailer:
            print(pointer.element)
            pointer = pointer.nxt


    
    
