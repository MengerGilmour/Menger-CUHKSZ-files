# Quene.py
class ListQueue:
    
    default_capacity = 100

    def __init__(self):
        self.__data = [None] * ListQueue.default_capacity
        self.__size = 0
        self.__front = 0
        self.__end = 0


    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            return self.__data[self.__front]

    #This method is added because we may want to visit the element in the end
    def end(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            return self.__data[self.__end-1]

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
            return None
        else:
            answer = self.__data[self.__front]
            self.__data[self.__front] = None
            self.__front = (self.__front + 1) % ListQueue.default_capacity
            self.__size -= 1
            return answer

    def enqueue(self,e):
        if self.__size == ListQueue.default_capacity:
            print('The queue is full.')
        else:
            self.__data[self.__end] = e
            self.__end = (self.__end + 1) % ListQueue.default_capacity
            self.__size += 1

    def __str__(self):
        #rearrange the self.__data starting from front
        rearrangeQueue=self.__data[self.__front:]+self.__data[:self.__front]
        return str([str(e) for e in rearrangeQueue if e != None])
    
    def __repr__(self):
        return str(self)

##test program:

q=ListQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
print(q)
