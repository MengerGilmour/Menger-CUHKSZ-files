from LBTree import LBTree

def pathOfTree(p,path):

    if (not p.left) and (not p.right):
        return 0     
    else:
        path = path + 1
        if p.left and p.right:
            return path + path + pathOfTree(p.left,path) + pathOfTree(p.right,path)
        elif p.left and (not p.right):
            return path + pathOfTree(p.left,path)
        elif (not p.left) and p.right:
            return path + pathOfTree(p.right,path)

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
    print(pathOfTree(tree.root,0))
main()
    
