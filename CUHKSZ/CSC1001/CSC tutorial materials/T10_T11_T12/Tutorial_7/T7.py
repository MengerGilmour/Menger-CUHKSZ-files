import random

##data type for key in dictonary
dict1 = {'a':1, 'b':20}
dict2 = {1:1, 2:20}
tup1 = (1,2)
tup2 = ('abc', 'xyz')
dict3 = {tup1:1, tup2:20}
#dict4={[1,2]:1, ['abc','xyz']:20}
print(dict1,'\n',dict2,'\n',dict3)


## string strip
str1 = '  abc   abc  '
str2 = ' abc    abc '
str3 = '#  #abc   abc  '
#remove all leading and tailing whitespace
print(str1.strip())
print(str2.strip())
#remove all leading and tailing character '#'
print(str3.strip('#'))



## randon number generation
#Generate a random number within [0,1)
a = random.random()
#Generate a random integer number within [0,10]
b = random.randint(0,10)
#Generate a random number within [0,10]
c = random.uniform(0,10) 
print(a,'\n',b,'\n',c)
