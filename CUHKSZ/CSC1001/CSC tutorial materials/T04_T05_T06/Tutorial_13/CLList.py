class Node:
    def __init__(self,element,pointer):
        self.element = element
        self.pointer = pointer

class CLList:
    def __init__(self):
        self.__tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            head = self.__tail.pointer
            return head

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            oldhead = self.__tail.pointer
            if self.__size == 1:
                self.__tail = None
            else:
                self.__tail.pointer = oldhead.pointer
            self.__size -= 1
            return oldhead

    def enqueue(self,e):
        newest = Node(e,None)
        if self.is_empty():
            newest.pointer = newest
        else:
            newest.pointer = self.__tail.pointer
            self.__tail.pointer = newest
        self.__tail = newest
        self.__size += 1
