from LBTree import LBTree

def evaluate(t):
    if not t.left and not t.right:
        return int(t.element)
    else:
        if t.element=='+':
            t.element=evaluate(t.left)+evaluate(t.right)
            return t.element
        elif t.element=='-':
            t.element=evaluate(t.left)-evaluate(t.right)
            return t.element
        elif t.element=='*':
            t.element=evaluate(t.left)*evaluate(t.right)
            return t.element
        elif t.element=='/':
            t.element=evaluate(t.left)/evaluate(t.right)
            return t.element
        
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
    print(evaluate(tree.root))
    
main()

