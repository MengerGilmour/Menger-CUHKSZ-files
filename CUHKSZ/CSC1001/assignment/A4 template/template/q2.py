"""
You are only permitted to write code between Start and End.
Don't change the template. Otherwise, you will get zero point.
"""


## Here you can write some extra code if needed, or you can igore this block.
# Start writing your code.

# End writing your code.


class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        # Start writing your code.
    
        # End writing your code.


    ## Here you can write some other functions inside the class if needed, or you can igore this block.
    # Start writing your code.

    # End writing your code.
    

def quick_sort(node):
    # Start writing your code.
    
    # End writing your code.


# We will write code as follows to check your answer. You can remain or delete the following code in the submission. Because the following code will be rewritten when checking your answer.
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [4,2,3,1,0,5]  # An example. We will change it during testing.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    p = quick_sort(first_node)
    while p.pointer != None:
        print(p.element)
        p = p.pointer
    print(p.element)


    def insert(self, data):
        # Start writing your code.
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.pointer = new_node
        self.tail = new_node
        self.size += 1
        # End writing your code.
    
