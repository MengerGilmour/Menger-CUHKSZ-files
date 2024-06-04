#1.求a,b之间的所有素数,一行打印5个数：for循环嵌套，def（）的应用
count=0
def sushu(n):
    for i in range(2,n):
        judge=True
        if n%i==0:
            judge=False
            break
    if judge==True:
        return n #为什么print(n)不可行--因为下面的for循环中用了sushu（），其实相当于两个for循环嵌套，如果print将跳出循环
    #每一次都会打印出来，下面的count其实就没什么用了，结果将会是一列素数而不是五个一行。而return（）是在循环里返回的，不会打印出来
#print(sushu(67))
a=int(input("enter an integer:"))
b=int(input("enter an integer which is bigger than a:"))
for i in range(a,b+1):
    if sushu(i)==i: #注意，运用sushu（）已经相当于循环嵌套！！！
        count=count+1
        if count%5==0:
            print(i)
        else:
            print(i,end=" ") #有end=“ ”就可以打印成一行
#output=
#53 59 61 67 71
#73 79 83 89 97
#101 103 107 109 113
#127 131 137 139 149

#2.输入三个数，并且从小到大排列-知识点：list,sort
x=float(input("enter a float:"))
y=float(input("enter a float:"))
z=float(input("enter a float:"))
a=[]
a.append(x)
a.append(y)
a.append(z)
b=sorted(a) #or print(a.sort())
print(b)

#3.求某个自然数的阶乘 知识点：for循环，recursion
#for loop
a=int(input("enter an integer:"))
times=1
for i in range(1,a+1):
    times=times*i
print(times)
#recursion method
def fac(n):
    if n<0:
        print('invalid input')
        return None
    elif n==0:
        return 1
    else:
        return fac(n-1)*n
print(fac(4))


#4.1,2,3,4能组成多少个互不相同且无重复数字的三位数？各是多少？ 知识点：for循环与len（）的应用/recursion
#三个for嵌套同时加上无重复数字的条件
list=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and a!=c and b!=c:
                A=a,b,c
                list.append(A)
                print(a,b,c,sep="")
print(len(list))

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

#5.编写程序，打印九九乘法口诀表
#用count解决
for i in range(1,10):
    count=0 #容易忽视 由于当i的值改变立刻需要换行，所以对每一个i都应该令count=0
    for j in range(1,i+1):
        count+=1
        A=i*j
        if count==i:
            print(f'{i}*{j}={i*j}')
        else:
            print(f'{i}*{j}={i*j}',end=" ")
#不用count：最优解
for i in range(1,10):
    print() #语法：换行
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end=" ")
#更方便的方法：倒序
for i in range(1,10):
    for j in range(1,10-i+1):#第一次要有九列，且要与“i”有关系，所以后面为10-i+1
        print(10-i,"*",j,"=",(10-i)*j,end="\t") #在python中,“\t”是指制表符,代表着四个空格,也就是一个tab;它的作用是对齐表格数据的各列,可以在不使用表格的情况下,将数据上下对齐。
    print(" ")
#补充：f-string
#使用f-string的基本语法非常简单，只需在字符串前面加上字母"f"，然后在字符串中使用大括号"{}"来包裹要插入的内容。
#变量被封装在大括号内，并在输出时被替换为它们的实际值。f-string会自动将变量的值插入到字符串中，表达式输出时也会被计算结果
# f-string还提供了一些格式化选项，以便更好地控制输出结果的格式。以下是一些常用的格式化选项：
# :d：将变量格式化为整数。
# :f：将变量格式化为浮点数。
# :.nf：将浮点数格式化为指定位数的小数。
# :s：将变量格式化为字符串。
num = 42
print(f"The number is {num:d}.")
# 输出结果为：The number is 42.

pi = 3.141592653589793
print(f"The value of pi is approximately {pi:.2f}.")
# 输出结果为：The value of pi is approximately 3.14.

name = "Alice"
print(f"Hello, {name:s}!")
# 输出结果为：Hello, Alice!
#除了简单的变量和表达式外，f-string还支持嵌套和复杂的表达式。可以在大括号内嵌套其他大括号来实现复杂的字符串格式化。
name = "Alice"
age = 25
print(f"My name is {name.upper()} and I'm {age} years old.")
#输出结果为：My name is ALICE and I'm 25 years old.

#6.找出所有水仙花数：三位数，各位数字立方和等于该数字本身
#method1
for i in range(100,1000):
    sum=0
    for a in str(i):
        sum=sum+(int(a))**3 #经过一整个循环过程得到一个sum值
    if sum==int(i): #注意这里不能缩进。在每次计算完sum后，应该在内层循环结束之后进行判断，并且需要将判断的语句放在外层循环中。
        print(int(i))
#method2
for i in range(100,1000):
    a=i%10
    b=(i//10)%10
    c=(i//10)//10
    if a**3+b**3+c**3==i: #这里需要缩进，因为是在if内部进行计算。如果把计算式放在for循环中，将不需要缩进
        print(i)
#7.输入字符，判断是否为字母:应用和string相关的函数isalpha（）
a=input("enter a string")
if a.isalpha()==True: #注意a.isalnum()判断是否只有字母和数字，a.isdigit()判断是否只有数字
    print("all letters")
else:
    print("not all letters")

#8.输入三组数据，看能否组成三角形的三条边:应用绝对值函数abs（）
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a+b>c and a+c>b and b+c>a and abs(a-b)<c and abs(a-c)<b and abs(b-c)<a:
    print("can form a triangle")
else:
    print("fail")

#9.一个数如果恰好等于除了它之外的因子之和，这个数就称作“完数”。请找出1000以内的所有完数（6就是，6=1+2=3)
for i in range(1,1000):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
            if sum==i:
                print(i)
#10.输入一个正整数，输出它的所有质数因子（比如180的质数因子为2,2,3,3,5）：创建list以及while循环
a=int(input("enter a positive integer:"))
y=2
list=[]
while a!=y:
    if a%y==0: #不可能出现除以2有除以4的情况：通过while循环会把2除尽。
        list.append(y)
        a/=y##
    else:
        y+=1
else:
    list.append(y)
for i in list:
    print(i,end=" ")
#a=120,output=2,2,2,3,5

#11.输入某年某月某日 判断这一天是这一年的第几天
year=int(input("enter a year:"))
month=int(input("enter a month(1-12):"))
day=int(input("enter a day(1-31):"))
if year%2==0:
    daysinmonth=[31,29,31,30,31,30,31,31,30,31,30,31] #运用一个tuple或者list来对应每个月的天数。
    sum=0
    for i in range(1,month):
        sum=sum+daysinmonth[i-1]
    sum=sum+day
    print(sum)
elif year%2!=0:
    daysinmonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    sum=0
    for i in range(1, month):
        sum = sum + daysinmonth[i - 1]
    sum=sum+day
    print(sum)
#12.编写找出斐波那契数列的第n项（斐波那契数列没有一个简单的单项公式）
#method1:运用递归 (效率很低，数字大的话函数调用次数太多)
def feibo(n):
    if n==1 or n==2:
        return 1 #如果是让feibo（n）=1，不能像左边这样return，return只能return一个变量的值
    else:
        return feibo(n-1)+feibo(n-2)
print(feibo(7))
output=13

#method2：非递归，用for循环加列表来不断填充斐波那契数列
n=int(input("enter a positive integer:"))
feibo=[1,1] #关键：创建一个初始列表[1,1]
for i in range(1,n):
    a=feibo[i]+feibo[i-1]
    feibo.append(a)#填充
print(feibo[n-1])

#13.将a列表复制给b列表：python中的深拷贝与浅拷贝
#浅拷贝,b=a,change in a will cause change in b
a=[1,2,3]
b=a
a.append(5)
print(a)
print(b)
#output=
[1, 2, 3, 5]
[1, 2, 3, 5]

#深拷贝 运用copy.copy()，这样列表将会互不相关。
a=[1,2,3]
b=copy.copy(a)
a.append(5)
print(a)
print(b)
#output=
a = [1, 2, 3, 5]
b = [1, 2, 3]

#14.输入一行字符，分别统计其中的英文字母、空格、数字和其他字符个数
a=input("enter a line of strings:")
count_letters=0
count_none=0
count_others=0
for i in a:
    if i.isalpha():
        count_letters+=1
    elif i==" ":
        count_none+=1
    else:
        count_others+=1
print(count_letters)
print(count_none)
print(count_others)

#15.一球从100m高度自由落下，每次落地后反弹回原来高度的一半再落下，求它在第十次落地时共经过多少米？第十次反弹多高？
h=100
sum=100
count=1
list1=[]
list2=[]
while count<=10:
    sum = sum + h
    h/=2
    list1.append(h)
    list2.append(sum)
    count+=1
print(list1,list2)

#15.打印2/1,3/2,5/3，...这个数列的前二十项之和。
up=2#
down=1#
count=0
sum=0
while True:
    a=up/down
    sum+=a
    count+=1
    if count==20:
        break
    a=up
    up+=down
    down=a #构造新的up和down值
print(sum)
output=32.66026079864164

#16.求1！+2！+3!+...+20!的和
sum=0
for i in range(1,21):
    a=1
    for j in range(1,i+1):
        a*=j
    sum+=a #特别留意这一步必须要跳出这个for循环，因为a必须是for循环进行完毕后阶乘的结果。
print(sum)
output=2561327494111820313
#补充
#求阶乘函数
#method1：using a for loop
i=int(input("enter a number:"))
a=1
if i<0:
    print("invalid")
if i==0:
    print("1")
else:
    for j in range(1,i+1):
        a*=j
    print(a)
#method2:using recursion 递归，层层递进
def facFunc(n):
    if n<0:
        print("invalid")
    if n==0:
        return 1
    else:
        return n*facFunc(n-1)
print(facFunc(3))



#17.打出一个3乘3矩阵并计算对角线数字之和
list=[ ]
n=0
while True:
    a=input("enter a number:")
    list.append(a)
    n+=1
    if n==9:
        break
count=0
for i in list:
    count+=1
    if count%3==0:
        print(i)
    else:
        print(i,end=" ")
sum=float(list[0])+float(list[2])+float(list[4])+float(list[6])+float(list[8])
print(sum)
#标答:创建一个二维列表，利用坐标表示（索引），更简洁高效
a=[] #表示大矩阵
sum=0
for i in range(3):#i在矩阵中代表行
    a.append([])#表示在这个矩阵中新放入一行
    for j in range(3):#j代表列
        k=int(input("enter a number:"))
        a[i].append(k)
        if i==j:
            sum+=a[i][j]#二次索引，二维列表用两次索引
print(a)
print(sum)
#用坐标确定矩阵上的数据，如第一行第一列就是（0,0）。发现主对角线上的数据坐标横纵坐标均相同。
output=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
15
#18.往有序列表中添加数据
list=[1,3,6,90]
i=float(input("enter a number"))
list.append(i)
list1=sorted(list) #或者list.sort()
print(list1)

#19.ef求最大公因数gcd
def gcd(n1,n2):
    gcd=1
    k=2
    while k<=n1 and k<=n2:
        if n1%k==0 and n2%k==0:
            gcd=k
        k+=1 #无论是否满足if条件，对下一个k的检验都必须是k+1，所以这一步要放在if判断句之外！
    return gcd
n1=int(input('enter the first integer:'))
n2=int(input('enter the second integer:'))
print('the greatest common divisor for',n1,'and',n2,'is',gcd(n1,n2))

#数组里没出现过的数字
list=[2,1,4,5,1,2]
#method1:散装写法
a=max(list)
N=len(list)
new_list=[]
for i in range(1,N+1):
    if i not in list:
        new_list.append(i)
print(new_list)
#method2：用def的写法，更规范
def func(list):
    l1 = [i for i in range(1, len(list) + 1)]
    l2 = []
    for i in l1:
        if i in list:
            continue #复习continue，重新进入循环
        else:
            l2.append(i)
    return l2
print(func([2, 1, 4, 5, 1, 2]))

#将字符串中的空格替换为‘%’
#method1
string=input('enter a string')
list=string.split(" ")
new_string= "%".join(str(x) for x in list) #将列表转化为字符串：string="(分隔符)".join(str(x) for x in list(列表名))
print(new_string)
#method2
def change(string):
    res=""#创建一个空字符串，直接往里面塞，不用考虑改变原字符串的内容，更加直接
    for i in string:
        if i != " ":
            res+=i ##
        else:
            res+="%" ##
print(change("a pp le"))

#use oop to print out the first 50 primes
def isprime(number):
    divisor=2
    while divisor<=number//2:
        if number%divisor==0:
            return False
        divisor+=1
    return True
def printPrimes(numberofPrimes):
    numberofPrimes_in_a_line=int(input('enter number of primes in a line:'))
    number=2
    count=0
    while count<numberofPrimes:
        if isprime(number):
            count+=1
            print(number,end=' ')
            if count%numberofPrimes_in_a_line==0:
                print() #换行
        number+=1
printPrimes(50)

