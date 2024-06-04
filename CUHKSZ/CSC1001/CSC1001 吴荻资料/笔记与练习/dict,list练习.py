#放入一些词并利用字典数一个词出现了多少次
count = {} #创建一个空字典
while True: #continuously input sth.:利用while True这个loop
    a = input("enter a word:")
    if a == "break":
        break
    if a in count:
        count[a] += 1 #注意格式正确，应该是dic[a]
    else:
        count[a] = 1
print(count)
#a much easier way using get method:
count = {}
while True:
    a = input("enter a word:")
    if a == "break":
        break
    count[a]=count.get(a,0)+1#参与这个循环，如果未输入过就是0，输入过就是该key对应的value+1 (注意，else可以省略）
print(count)
#for example the output will be like:
#enter a word:a
#enter a word:c
#enter a word:c
#enter a word:bb
#enter a word:bb
#enter a word:a
#enter a word:d
#enter a word:break
#{'a': 2, 'c': 2, 'bb': 2, 'd': 1} 也就是说print(count)的结果就是一个字典的形式


#输入一个text并利用字典数一个词出现了多少次
text=input("enter a text:")
a=text.split() #用split()将text拆分成一个字符串的list #注意split（）将会生成一个列表
counts={} #不要忘记创建一个空字典
for i in a:#use a for loop to count
    counts[i]=counts.get(i,0)+1
print(counts)
print(counts["a string you want to count"])

#根据每个元素的值对元素进行排序
dic={"d":3,"b":2,"c":44}
a=[]
for key,value in dic.items():
    a.append((value,key)) #调换顺序，内部是tuple要用（，）
a.sort(reverse=True) #数字倒序，从大到小排
print(a)
output=[(44, 'c'), (3, 'd'), (2, 'b')]


#利用字典找到文件里出现次数最多的词语
a=open("eee.txt","r") #打开该文件
c={}
for line in a: #拆分文件的每一行得到分散的词语，然后数这些词出现的次数（for循环嵌套，因为是一句一句拆分数词语）
    words=line.split()
    for word in c:
        words[word]=words.get(word,0)+1
b=[]
for key,value in c.items(): #按数字大小顺序排列则需要将（key，value）变成（value，key）然后放进list里用sort解决
    b.append((value,key)) #里面的括号不要忘记！创建tuples
b.sort(reverse=True) #tuple不可用sort排序方法，只有列表才可以
for value,key in b[0:10]: #不能直接打出b[0：10]，要再次将(value,key)反过来变成(key,value)
    print(key,value)

#write a program that reads some integers between 1 and 100 and counts the occurrences of each
list=[]
count={}
while True:
    a=input("enter an integer between 1 and 100:")
    if int(a)<1 or int(a)>100:
        print("error,enter again")
    if a=="stop":
        break
    count[a]=count.get(a,0)+1
for (key,value) in count.items():
    if value>1:
        print(key,"occurs",value,"times")
    else:
        print(key,"occurs 1 time")

#write a program that reads in numbers separated by a space in one line and displays distinct numbers.
inp=input("enter 10 numbers separated by a space in one line:")
list1=inp.split()
list2=[]
for num in list1:
    if num not in list2:#新语法学习：not in;如果出现过的话就不会加到list2里面了！！
        list2.append(num)
print("the distinct numbers are:",end="")
for num in list2:
    print(num,end=" ")
#compute the standard deviation of n numbers
list=[]
count = 0
sum = 0
while True:
    x = input("enter numbers:")
    if x == "stop":
        break
    count += 1
    sum = sum + float(x)
    list.append(float(x))

def mean(x):
    return sum/count
def deviation(x):
    sum1=0
    for i in list:
        a=(i-mean(x))**2
        sum1=sum1+a
    print((sum1/(count-1))**0.5)
    print(sum/count)
mean(x)
deviation(x)

#test sorted list
#如果你想指示用户输入一个列表，你可以使用input()函数配合split()函数来实现。
#input()函数可以让用户在命令行中输入一段文字，而split()函数可以将这段文字分割成一个列表。
a=input("print some numbers and divide them by commas:")
list1=a.split("，")
def isSorted(list1):
    if list1==sorted(list1):
        print("True")
    else:
        print("False")
isSorted(list1)
