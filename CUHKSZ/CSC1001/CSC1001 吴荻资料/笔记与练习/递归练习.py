#q1 number system conversion
#1.1将十进制转换为其它base：理解原理，应用递归
def conv(n,base):
    if n//base==0: #如果商为0，直接打印本身
        print(n,end='')
    else:
        conv(n//base,base) #商不为0，整除
        print(n%base,end='') #打印余数，用求余。这种递归构造下就是从下往上看的顺序！！
conv(12,2)
output=1100
#为什么不是0011呢？因为根据递归，第一次递归的结果是conv(6,2),print(12%2,end='')，但是conv(6,2)又会调用递归，所以实际上输出的顺序是1100，而不是0011，几个print的顺序是从上往下的

#1.2利用递归打印一个数的每一位
def printdigit(n):
    if n//10==0:
        print(n)
    else:
        printdigit(n//10)
        print(n%10)

#1.3利用递归反转一个数
def reverse(n):
    if n//10==0:
        print(n,end='')
    else:
        print(n%10) #和上题相比其实就是调换了最后两步的顺序，call递归的位置不一样，那么打印的顺序也不一样，理解好！！
        reverse(n//10,end='')
#利用递归反转一个字符串：
def reverse(s1,s2):
    if s2=='':
        print(s1)
    else:
        s1 += s2[len(s2)-1]
        s2 = s2[:len(s2)-1]#注意是左闭右开的形式,不是[:len(s2)-2]
        reverse(s1,s2)
reverse('',"apple")
output=elppa
#q2 all permutations of a string：打印一个元素的所有排列可能
def permutationhelper(s1,s2):
    if s2=='': #当s2中的所有元素进入s1，打印
        print(s1)
    else:
        for i in s2: #s2中的每一个元素都有机会做开头，所以要用一个循环
            index=s2.index(i) #index是一个数字
            permutationhelper(s1+i,s2[:index]+s2[index+1:]) #利用递归，s2要扣掉i
def main():
    s=input('enter a string:')
    permutationhelper(' ',s)
main()

#q3：judge palindrome判断是否为回文字符串
def check(s):
    if s=='': #如果检查完毕都不出错，return True，确实是回文
        return True
    elif s[0]==s[len(s)-1] and check(s[1:len(s)-1]):#同时满足两个条件；首尾一组一组检查,不断重构（截取）新的列表检查
        return True
    else:
        return False
def main():
    s=input('enter a string:')
    print(check(s))
main()

#q4；rearrange a list:所有偶数排列在奇数之前

list2=[]
def rearrange(list):
    for i in list:
        if i%2==0:
            list2.append(i)
            list.pop(list.index(i)) #注意语法，list.pop(index)，而list.index(string)将返回所求string的index
            rearrange(list)#运用递归，不断在缩小list范围时pop出偶数
    return list2+list
print(rearrange([1,4,3,2]))
output=[4,2,1,3]

#q5：这个函数findsubset的目的是找到一个列表L的所有子集，并将这些子集添加到一个列表T（初始为空列表）中。
def findsubset(L,T):#L是输入的列表，T是创建的一个用来储存子集的空列表
    if len(L)==0: #子集为空集，返回空集，结束程序
        return []
    for i in range (len(L)): #range左闭右开
        subset=[] #在每次循环开始时，创建一个空列表subset，用于储存子集元素
        for element in L:#遍历列表L中的每一个元素
            if element!=L[i]:#注意理解：如果当前元素的索引不等于外部循环的索引i指示的元素
                subset.append(element)#则将该元素添加到subset列表中，构建一个不包含当前元素的子集
        if subset not in T: #如果subset列表不在结果列表T中，说明子集是新的
            findsubset(subset,T)#递归调用find_subsets函数来生成更小规模的子集，注意是T不是L,一直到subset（L）成为一个空集，return。
            T.append(subset)#往列表T中添加子集列表（也就是列表中的元素是小列表）
    return T
L=[1,2,3]
print(findsubset(L,[]))