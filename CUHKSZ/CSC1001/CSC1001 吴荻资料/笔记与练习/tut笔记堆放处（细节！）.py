#tut笔记 L1L2
#reminder：如果撤销修改ctrl+Z;如果全部变成comments则ctrl+？、键
#basic:
print("1"+"2")
output=12
print("1"+2)
output=error
print(eval('1'+'2'))
output=12
print(eval("1+2")) #eval（）去掉参数最外层括号并执行余下语句
output=3
#1.地址与值不同  查找id用id（）
a=[1,2,3]
b=[1,2,3]
print(a==b)
output=True
print(a is b)
output=False
#于此相对比
a=1
b=1
print(a==b)
output=True
print(a is b)
output=True
a=1
b=1.0
print(a==b)
output=True
print(a is b) #"is" statement is stronger and the types of a and b are different although there values are the same
output=False

a=[1,2,3]
b=a
b[0]=0#a,b的value和address均相同
print(a)
print(b)
#重复以上两个print，结果都为True

#2函数总结
#len()函数 得到字符串的长度
#lower(),upper()字符串全部大写转小写或者小写转大写
a="HIGH"
B=a.lower() #注意格式
print(B)
output=high
#a.startswith()判断字符串是否以()内的内容开始--return Ture or False
#handle=open("filename","r读/w书写/a append"),print(handle)
#find(string,[start],[end])找到所求字符串第一次出现的位置
a="apple app" #string position starts from 0,空格也占一个位置
b=a.find("app")
print(b)
output=0 #remember the index starts from 0
#list.append(新元素)  向列表中追加新元素，也可向一个列表中嵌套新的列表(在尾部追加)//如果要在某一个位置之前插入一个新元素，用list.insert(位置，新元素)(只是对原列表进行操作，不会返回新列表，插入成功将返回None）
#若要将list中某个元素改掉：list[location(using index operator)]=new item
a=[1,2,3,44,66]
b=a.insert(2,100)
print(a)
output=[1,2,100,3,44,66]
print(b)#这是对原列表的操作 不会返回新列表
output=None #(说明插入成功)
#list.sort()重新排序
#replace("a","b") 也就是replace("定位","替换")
a="apple,pie"
b=a.replace("apple","peach") #注意都是字符串，要用引号框起来
print(b)
output=peach,pie
#lstrip()取消左侧空格 rstirp()取消右侧空格 strip()同时取消左右两侧空格
#range()函数 创建一个整数列表  (start,stop,step) 但不包括stop，如需要应该输入（stop+1）
range(10)
0,1,2,3,4,5,6,7,8,9
range(0,10,3)#步长为3
0,3,6,9
range(0,-10,-1)
0,-1,-2,-3,-4,-5,-6,-7,-8,-9
list(range(5))
[0,1,2,3,4]
print(range(1,10))
output=range(1,10)
print(list(range(1,10)))
output=[1,2,3,4,5,6,7,8,9]
#字符串函数 str()
str(1)+str(1)+str(1)
output='111'
#def()自定义函数  定义-内容-接收返回-print
#abs()返回绝对值
#min() max()返回最小值、最大值
min(1,2,3,4,5)
output=1
#sum()求和--利用list[]才能多个求和
sum([1,2,3,4,5])
output=15
#list()
list('apple')
output=('a','p','p','l','e')
#sep=''间隔函数
print(1,2,3,4,5,sep='*')
output=1*2*3*4*5
print(1,2,3,4,5,sep='\n') #注意表示换行      #如果要得到\n或者\t，应该print（\\n,\\t)
1
2
3
4
5
#max() min() 若输入字符串则为ASCII Code（一种计算机编码系统，用于表示文本中的字符，包括字母、数字和符号）
print(1,2,3,4,5,sep='\t') #表示空开
#output=1     2     3     4     5

#type()查询类型   #float()变小数--字符串不可加减乘除，有时候要通过该函数转换成小数才能继续  #int()变整数    #input("")用于指导操作
#printf函数格式字符:%d,i 以带符号的十进制形式输出整数;%f 以小数形式输出单，双精度数，隐含输出6位小数
a=pi#π
print(a)
print('%i'%a)
print('%8d'%a) #从左边开始补。取整数只有一位，于是用空格来代替，8指的是结果一共占用八个位置（空格、符号、字母或者数字），"."也占一个位置
print('%-8d'%a) #有负号，右边
print('%.5f'%a)#即保留五位小数1
print('%8.4f'%a)
print('%s'%a) #%s在python中的意思是用作print的格式化输出：打印字符串
output
3
-------3(#前面空开七位)
3-------
3.14159
--3.1416
3.141592653589793
#divmod()返回商与余数
x,y=divmod(5 ,4)  #结果为x=1,y=1，返回一个tuple

#eval() 主要用来实现python中各种数据类型与str之间的转换，也可以直接实现字符串的计算
#eval("5+2+3")=10
#易错：eval（“‘1’+‘2’”）=12 先里后外，即eval("12")


#3.运算符号总结
#x+=1 即为 x=x+1
# %为返回除法的余数：特别注意，如果有负数参与：-9%4=-9-（-9//4)*4=3; 9%-4=9-(-9//4)*-4=-3, 其中-9//4=-3 (相反数）
# //为向下取整数，即取不大于该数的最大整数(floor division)
#优先级一样，从左到右计算

#4.for循环 以及 while循环 loop
#for循环--（关键词）元组，列表，字典，字符串，集合，range，break终止整个循环，pass（占位）跳过执行下一个语句，continue跳出当前循环执行新的循环
#格式：for变量名in可遍历变量
#举例（应用continue）
names="applepie"
for name in names:
    if name=="l":
        continue
    print(name)
output=
a
p
p
e
p
i
e
#for\while循环的嵌套
#以两层循环为例：外层循环，进入内层循环后完全执行内层循环，然后在进入外层循环，以此类推
list=[1,2,3]
for i in "app":#enter the outer loop
    for n in list:#finish the inner loop
        print(n)
    print(i)
#output=
1
2
3
a
1
2
3
p
1
2
3
p

n=0
while n<3:
    print(n)
    n+=1
    count=0
    while count<2: #先把内层循环执行完，再回到外层循环，以此类推
        print(count)
        count+=1
print("finished")
#output=
0
0
1
1
0
1
2
0
1
finished
#练习
#给定一个数字列表，将其中的奇数和偶数分开。
numbers=[23,24,2,6,55,89,100]
jishu=[] #这一步给列表命名
oushu=[]
for i in numbers:
    if i%2==0:
        oushu.append(i) #利用list.append(item)将数字放进列表中
    else:
        jishu.append(i)
print(jishu) #一定要将两个列表打印出来，才有结果
print(oushu)

#验证任意一个大于9的整数减去它的各位数字之和（运用for循环）所得的差一定能被9整除
integer=input("enter an integer which is bigger than 9")
sum=0
for i in integer:
    sum1=int(i)
    sum=sum+sum1
print(sum)
b=int(integer)-sum
if b%9==0:
    print("OK")
else:
    print("ERROR")
print("DONE")
#while循环(infinite loop)--（关键词）元组 列表 字典 字符串 集合 break终止循环 else pass跳过 continue继续执行
#简单示例以及死循环的理解
n=5
while n>0:
    print(n)
    if n==3:
        continue
    n-=1 #这个不能放在循环体后面，不然会进入死循环，应该放在if语句之前
else:
    print("done")
#最终的结果会是5,4,3,3,3,3,3,3,3,3,3...陷入了一个循环：因为当n第一次等于3，continue继续执行循环，也就是n带着3这个值重新参与到while循环里，
#在第一步不断print，于是不断死循环；；若把continue换成break，那么这个循环到n=3就会跳出循环，n-=1和else语句也不会被执行。最终的结果是543，2和1不会被打印
#在loop中，break指的是结束该层循环（跳出最内层的循环，向外跳一层）；continue跳出当前循环的剩余语句，继续进行下一轮循环；pass表示站位，什么都不做，pass后面的语句还会继续执行.
#给定一个数字列表，将其中的奇数和偶数分开。
numbers=[23,24,2,6,55,89,100]
jishu=[]
oushu=[]
while numbers:#当列表不为空
    num=numbers.pop() #pop()指的是从这个数集中取出一个数
    if num%2==0:
        oushu.append(num)
    else:
        jishu.append(num)
print(jishu)
print(oushu)

#5.元组tuple与列表list
#索引：从左往右为012345...;从右往左为-1-2-3-4...
#应用tuple
a=(1,2,3,4,5)
a[2]
output=3
a[1:3]
output=2,3
a[-4]
output=2
#补充：在tuple中应用len(),count(),index()
a=(1,2,3,4,5)
len(a)
5
a.count(3)
1
a.index(4) #index()用于查找元素的索引
3
#应用list：注意tuple无法更改元素而list可以更改
a=[1,2,3,4,5]
a[0]=10
print(a)
output=[10,2,3,4,5]
#list的基本操作：增加元素用list.append(new item)\list.insert(location,new item)、删除元素用list.remove(item)\list.pop(location)取出一个数\list.clear()全部删除
#其中list.insert(len(list).new item)等同于list.append(new item))
#sort()易错：对于一个已知列表a,对a排序的结果应该是a.sort(),print(a),而不是b=a.sort(),print(b),否则将返回None.

#6.if语句的嵌套（外部、内部）
#外层if不成立，跳出嵌套执行else；外层成立继续以后的if，关于运行的判断同左。

#课堂练习1.1：print a table(use formatted output of print function)
print('%-8s%-8s%-8s'%('a','b','a**b'))#制作表格的表头，注意s用于打印字符串
print('%-8d%-8d%-8d'%(1,2,1**2))#注意d用于输出整数，%后要用括号括起来
print('%-8d%-8d%-8d'%(2,3,2**3))
#将得到一个如下表格：
#a       b       a**b
#1       2       1
#2       3       8

#课堂练习1.2
celcius=float(input("write down a Celcius  degree"))
frahrenheit=(9/5)*celcius+32
print(frehrenheit)

#课堂练习2：将任意分钟转化为年 天 分钟；要求熟练运用%取余数以及//向下取整数
minutes=float(input("enter the number of minutes"))
a=float(minutes//(24*60))#a是有多少天
if a==0:
    print("less than a day",minutes,"minutes")
elif a>=1:
    b=float(minutes//(24*60*365))#b是有多少年
    if b==0:
        c=float(minutes%(24*60))#c是有多少分钟剩下
        print(a,"days",c,"minutes")#特别注意这个print要和变量表达式对齐 不然会运行失败
    if b>=1:
        d=float(a-b*365)
        e=float(minutes%(24*60*365))
        print(b,"years",d,"days",e,"minutes")
print("finished")

#课堂练习3：计算数位之和
#如何利用for循环迅速解决：
a=input("enter an integer:")
sum=0
for i in a:
    sum=sum+int(i)
print(sum)
#老师的方法 学习！！！！这个可能会应用在倒排一个数的程序里面（个、十、百、千位一步步推进就可以了 不用复杂化）
number=int(input('enter a number between 1 and 1000'))
sumup=0 #关键 定义为0
sumup=number%10 #个位
number//=10 #和+=，-=一样可以引申！新的number就变成了除掉个位的新数字
sumup+=number%10 #个位＋十位
number//=10 #新number变成了除掉个位和十位的新数字
sumup+=number%10 #个位+十位+百位
print("the sum up will be",sumup)
#优化老师方法 use a while loop
a=int(input("enter a number:"))
sum=0
while a!=0:
    b=a%10
    sum+=b
    a=a//10
print(sum)

#倒排一个数
#方法一：利用字符串
a=input("enetr a number:")
n=len(a)
print(n)
b=""
for i in range(n-1,-1,-1):
    b+=a[i]
print(b)
#方法二:利用切片
a=input("enter a number:")
b=a[::-1]
print(b)
#about range():
for i in range(0,3,-1):
    print(i)
#output=none,cause it is invalid
for i in range(3,0,-1):
    print(i)
#correct syntax,and now output=3,2,1
for i in range(-1,-10,1):
    print(i)
#if (-1,-10,1),no output; if (-1,-10,-1), the output will be from -1 to -10!
#be careful of the value of the step!!


#display a PYRAMID:write a program that prompts the user to enter an integer from 1 to 15 and displays a pyramid with height
#of that integer.数字金字塔（难：金字塔要求对称）
i=int(input("enter a number between 1 and 15:"))
for j in range(1,i+1):
    for z in range(0,5*(i-j)):
        print(" ",end="") #在每一行开始，这一行代码会打印适当数量的空格。这是为了确保数字在打印时能够正确地对齐。空格的数量随着行数的增加而减少。
    for a in range(j,0,-1):
        print('%5s'%a,end="") #将变量 a 的值格式化为一个至少5个字符宽的字符串，并在其后面添加一个空格
    for b in range(2,j+1):
        print('%5s'%b,end="")
    print(" ")#换行

#课堂练习5：用列表和while循环求平均数
list=[]
while True: #构建一个while循环 才能不断将数字添加到列表里面
    inp=input("enter a number:")
    try:
        float(inp)
        list.append(float(inp))
    except:
        if inp=="done":
            break
        else:
            print("reconsider:please enter a number")
print(sum(list)/len(list))

#tut def()练习题
#1.#输入一个数，判断是否为回文数并返回该数的reverse number：
def reverse(number):
    reversenumber = "" #创建一个空字符串
    while number!=0:  #此处再次应用while循环，将数一个个数位挑出来然后倒序放置
        reversenumber+=str(number%10) #先是字符串
        number=number//10 #类似之前的计算数位之和的操作！！关键易忘！！
    reversenumber=int(reversenumber)
    return reversenumber
#or we can simplify the previous program using [start,stop,step] like this:
def reversenumber(number):
    reversenumber=str(number)[::-1]
    print(reversenumber)
reversenumber(12783)
output=38721
#or we can use recursion to check whether it is a palindrome or not:
def checkreversenumber(s):
    if s=='':#每一组都对比完
        return True
    elif s[0]==s[len(s2)-1] and reversenumber(s[1:len(s)-1]):#首尾一组一组对照比较
        return True
    else:
        return False
def main():
    s=input('enter a number:')
    print(checkreversenumber(s))
main()


def ispalindrome(number): #创建一个新函数用于判断是否为回文数
    if number==reverse(number): #可以识别前面定义过的函数
        return True #注意应用布尔返回True和False
    else:
        return False

print(reverse(123321))
print(ispalindrome(123321))
output=123321,True

#如果要打出前100个回文数，只需要在前两个def函数的基础上加上如下程序：
count=0
for number in range(1,100000000):
    if count<=100 and ispalindrome(number): #if的嵌套，如果不满足第一个if将直接跳到print（“finished”）部分，不会执行下一个if
        count+=1
        if count%10==0: #要求十个一行，记住这个格式，常考
            print(number)
        else:
            print(number,end=" ") #这样才能打成一行而不是一列
print("finished")

#easy to make mistake in a while loop:
#嵌套循环进入第二个循环后会一直进行循环，所以如果加上while count<=100，将会在第二个循环内无限运行下去，可以参考assignment1的练习.

#课堂练习：关于string和file的训练
#1.找到一个字符串中所有“a”的位置序号
str=input("enter a string:")
i=0 #str.find(string,start,end)判断查询字符串中是否有含有目标字符串，有则返回第一个查询找到的位置，否则返回-1.
while str.find("a",i)!=-1: #从第一位开始找a，知道发现一个a存在，如果不存在python默认返回-1
    index=str.find("a",i) #index becomes the place where we find a
    print(index) #打出第一次出现a的位置
    i=index+1
else:
    print("none")
#2.define a function to check whether 'substring'is a substring of 'string'
def find(substring,string):
    index=0 #start from index 0 of the string
    for i in string:
        if i==substring[0]:  #看看string哪一个元素能与substring的第一个元素相同;能进入这个if语句说明此时i=string【index】=substring【0】
            if string[index:index+len(substring)]==substring: #cut the string with the length of 'substring' from 'string' to check whether they are the same
                return index
            else:
                index+=1
                continue
        index+=1 #如果string的第一个元素和substring的第一个元素不相等那么要跳到string的下一个元素开始对比，for循环中i已经加了1，index也应该加一
    return -1
#3.check a password:
#must have at least 8 characters,consist of only letters and digits,contain at least two digits
a=input("enter your password")
if len(a)>=8:
    print("valid")
else:
    print("invalid,your password must have at least 8 characters")
if not a.isalnum(): #string.isalnum()用于检查是否全都是字母和数字
    print("invalid,your password must consisit of only letters and numbers")
else:
    print("valid")
count=0
for i in a: #利用for循环一个个元素查找是否为数字
    if i.isdigit(): #string.isdigit()用于检测字符串中是否只包含数字字符，返回True或者False。isdigit函数没有参数
        count+=1
if count>=2:
    print("valid")
else:
    print("invalid,your passwod must contain at least 2 digits")
#use def():
def isvalidpassword(password):
    if len(password)<8:
        print("invalid")
        return False
    if not password.isalnum():
        print("invalid")
        return False
    count=0
    for i in password:
        if i.isdigit():
            count+=1
    if count<2:
        print("invalid")
        return False
    else:
        return True
#3.return the longest common prefix of 2 strings 返回s1，s2共同的最长前缀
def prefix(s1,s2):
    i=0
    s=s1[0]
    while i<=len(s1) and s2.startswith(s): #enlarge the prefix until it is not common 由于s要不断延长 应该用while循环
        i+=1
        s=s1[:i+1] #slicing the string to get prefix
    s=s1[:i] #得到最长前缀
    return s
def main(): #定义一个新函数指导输入s1，s2，
    s1=input("enter the first string:")
    s2=input("enter the second string:")
    print("the longest common prefix of the two strings is",prefix(s1,s2))
main() #main函数的应用就是这样 直接在外部打一个main（）唤醒即可

#OOP tut
#1.如何修改以下简单程序使之可以打印（两种思路，public或者private）
# What are problems of the following program?
class A:
   def __init__(self):
       self.__i=i
def main():
   a=A(5) #问题就出在这里，用了private不能从class外面直接access
   print(a.__i)
main()
#method1：Change to public and initialize data file i when constructin the object
class A:
    def __init__(self,i):
        self.i=i
def main():
    a=A(5)
    print(a.i)
main()
#method2:use a getter
class A:
    def __init__(self):
        self.__i=i
    def geti(self):
        return self.__i
def main():
    a=A(5)
    print(a.geti())
main()
#2.银行account：学习细节
class Account:
    def __init__(self,ID=0,balance=100,annualInterestRate=0):
        self.__ID=ID
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate
    def setId(self,ID=0): #set method（）可附上default value
        self.__ID=ID
    def setBalance(self,balance=0):
        self.__balance=balance
    def setAnnualInterestRate(self,annualInterestRate=0):
        self.__annualInterestRate=annualInterestRate
    def getId(self): #getter method后面都是return
        return self.__ID
    def getBalance(self):
        return self.__balance
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def getMonthlyInterestRate(self):
        MonthlyInterestRate=self.__annualInterestRate/12
        return MonthlyInterestRate
    def getMonthlyInterest(self):
        MonthlyInterest=self.__balance*self.getMonthlyInterestRate()/100 #不要忘记/100
        return MonthlyInterest
    def withdraw(self,ammount=0):
        self.__balance=self.__balance-ammount
    def deposit(self,ammount=0):
        self.__balance=self.__balance+ammount

def main():
    Alice=Account(1122,20000,4.5)
    print('-'*66) #制作一个表格
    print('%-8s%-12s%-26s%-18s'%('ID:','Balance:','Monthly interest rate(%):','Monthly interest:'))
    print(('%-8d%-12.2f%-26.2f%-18.2f')%(Alice.getId(),Alice.getBalance(),Alice.getMonthlyInterestRate(),Alice.getMonthlyInterest()))#由于是private，所以全部都要用getter才能access
    print('-'*66)
    Alice.withdraw(2500)#取出2500
    print('-'*66)
    print("After withdraw $2500:")
    print('%-8s%-12s%-26s%-18s'%('ID:','Balance:','Monthly interest rate(%):','Monthly interest:'))
    print(('%-8d%-12.2f%-26.2f%-18.2f')%(Alice.getId(),Alice.getBalance(),Alice.getMonthlyInterestRate(),Alice.getMonthlyInterest()))
    print('-'*66)
    Alice.deposit(3000)#放入3000
    print('-'*66)
    print("After deposit $3000:")
    print('%-8s%-12s%-26s%-18s'%('ID:','Balance:','Monthly interest rate(%):','Monthly interest:'))
    print(('%-8d%-12.2f%-26.2f%-18.2f')%(Alice.getId(),Alice.getBalance(),Alice.getMonthlyInterestRate(),Alice.getMonthlyInterest()))
    print('-'*66)

main()
#3.simulate an ATM machine
class Account:
    def __init__(self,balance=100):
        self.__balance=balance
    def setBalance(self,balance=0):
        self.__balance=balance
    def getBalance(self):
        return self.__balance
    def withdraw(self,ammount=0):
        self.__balance=self.__balance-ammount
    def deposit(self,ammount=0):
        self.__balance=self.__balance+ammount
    def exit(self):
        print('good bye!')
def main():
    A=Account()
    while True:
        ID=int(input("enter your ID:"))
        if ID<0 or ID>=10:
            print('enter a correct ID')
        else:
            print('Enter your ID:',ID)
            print('Main menu')
            print('1:check balance','2:withdraw','3:deposit','4:exit',sep='\n') #复习换行操作：sep='\n';空格为sep='\t'
            while True:
                b=int(input('choose a number from 1-4:'))
                print('-'*20)
                print('Eter a choice:',b)
                if b==1:
                    print('the balance is',A.getBalance())
                if b==2:
                    amount=float(input('enter an amount to withdraw:'))
                    print('enter an amount to withdraw',amount,A.withdraw(amount))
                if b==3:
                    amount=float(input('enter an amount to deposit:'))
                    print('enter an amount to deposit',amount,A.deposit(amount))
                if b==4:
                    print(A.exit())
                    break
main()
#4，易错辨析：__new__() and __init__()

class A:
    def __new__(self):
        self.__init__(self)
        print("A's __new__() invoked")
    def __init__(self):
        print("A's __init__() invoked")
class B(A): #虽然没有写明，但是B已经继承了A的new方法，而且new方法（实例化）会在init方法（初始化）之前被调用，所以B会先调用A中的new方法
    def __init__(self):
        print("B's __init__() invoked")
def main():
    b=B() #这一项的输出结果为output的前两行
    a=A()
main()
# output=
# B's __init__() invoked
# A's __new__() invoked
# A's __init__() invoked
# A's __new__() invoked

#5.不能通过子类直接访问父类的私有方法和属性，除非通过在子类中改写
class A:
    def __init__(self, i=0, j=0):
        self.__i = i
        self.j = j
    def __m1(self):
        self.__i += 1
    def m2(self):
        return self.__i
class B(A):
    def __init__(self, i=1, j=1): #子类、父类公有属性可以被子类访问并且修改，直接覆盖。
        super().__init__(i, j)#注意，括号内一定要写出i，j
b = B()
print(b.__i)    #①，crash
print(b.j)  # ② 1
print(b.__m1()) #③ crash
print(b.m2())  # ④ 1，相当于用了一个getter去访问父类中的self.__i
#易错辨析（关于调用super是否覆盖的问题）
#situation1
class A:
    def __init__(self,a=300):
        self.a=a
class B(A):
    def __init__(self,a=200):
        super().__init__(a) #改写了a的值（公共），直接覆盖
c=B()
print(c.a)
output=200
#situation2:
class A:
    def __init__(self,a=300):
        self.a=a
class B(A):
    def __init__(self,a=200):
        super().__init__() #没有覆盖掉a，仍然用父类中的值,super method调用父类accessible的data field和method
c=B()
print(c.a)
output=300
#特别神奇的，记住
class A:
    def __init__(self,i=0,j=0,k=0):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return "color"

class B(A):
    def __init__(self,i=1,j=3,k=4,M=9):
        super().__init__(i,k,M) #这个括号里面其实就是把上一行定义的数字放进来，不是和A中的i，k一一对应的，只会把数字给到对应位置的A中的参数。但是括号里面的字母必须是B中定义过的，不然会报错
    def display(self):
        print(self.__str__())
b=B()
print(b.i)#1
print(b.j)#4
print(b.k)#0
print(b.display())#color
print(b)#color
#name mangling：涉及到父类私有方法，如果不改写，那么私有方法将带上父类的tag
class Person:
    def __getinfo(self):
        return "person"
    def printperson(self):
        print(self.__getinfo())
class Student(Person):
    def __getinfo(self):
        return "student"
    # def printperson(self):
    #     print(self.__getinfo())
Person().printperson() #person
Student().printperson() #person (#student)

#muliple inheritance多重继承的处理方法
class A:
    def __init__(self,a=100):
        self.a=a
class B:
    def __init__(self,b=200):
        self.b=b
class C(A,B):
    def __init__(self,a,b,c=300):
        A.__init__(self,a)
        B.__init__(self,b)#必须要有这个self，注意书写格式
        self.c=c
    def output(self):
        print(self.a)
        print(self.b)
        print(self.c)
def main():
    c=C(1,2,3)
    c.output()
main()







