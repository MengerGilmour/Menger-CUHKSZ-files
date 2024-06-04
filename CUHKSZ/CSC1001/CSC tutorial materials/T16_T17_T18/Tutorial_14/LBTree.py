class Node:

    def __init__(self,element,parent = None,left = None,right = None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right

class LBTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def find_root(self):
        return self.root

    def parent(self,p):
        return p.parent

    def left(self,p):
        return p.left

    def right(self,p):
        return p.right

    def num_child(self,p):
        count = 0
        if p.left is not None:
            count += 1
        if p.right is not None:
            count += 1
        return count

    def add_root(self,e):
        if self.root is not None:
            print('Root already exists.')
            return None
        self.size = 1
        self.root = Node(e)
        return self.root

    def add_left(self,p,e):
        if p.left is not None:
            print('Left child already exists.')
            return None
        self.size += 1
        p.left = Node(e,p)
        return p.left

    def add_right(self,p,e):
        if p.right is not None:
            print('Right child already exists.')
            return None
        self.size += 1
        p.right = Node(e,p)
        return p.right

    def replace(self,p,e):
        old = p.element
        p.element = e
        return old

    def delete(self,p):
        old = p.parent
        if p.parent.left is p:
            p.parent.left = None
        if p.parent.right is p:
            p.parent.right = None
        return old
