from LBTree import LBTree
from DFS import DFSearch
from BFS import BFSearch

def main():
    tree=LBTree()
    t11=tree.add_root('-')
    t21=tree.add_left(t11,'*')
    t22=tree.add_right(t11,'/')
    t31=tree.add_left(t21,'2')
    t32=tree.add_right(t21,'-')
    t33=tree.add_left(t22,'8')
    t34=tree.add_right(t22,'+')
    t41=tree.add_left(t32,'5')
    t42=tree.add_right(t32,'4')
    t43=tree.add_left(t34,'1')
    t44=tree.add_right(t34,'3')

    print('Depth First Search:')
    DFSearch(tree.root)
    print('Breadth First Search:')
    BFSearch(tree.root)
    
main()

