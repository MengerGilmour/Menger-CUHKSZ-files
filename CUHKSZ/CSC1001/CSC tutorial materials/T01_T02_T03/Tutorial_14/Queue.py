class ListQueue:

    def __init__(self,capacity):
        self.__capacity = capacity
        self.__data = [None] * self.__capacity
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

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
            return None
        answer = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        return answer

    def enqueue(self,e):
        if self.__size == self.__capacity:
            print('The queue is full.')
            return None
        self.__data[self.__end] = e
        self.__end = (self.__end + 1) % self.__capacity
        self.__size += 1

    def __str__(self):
        return str(self.__data)
    def __repr__(self):
        return str(self)
