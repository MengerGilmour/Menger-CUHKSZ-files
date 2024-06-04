# TUTORIAL 2 - PYTHON BASICS (20 SEPTEMBER 2023), CREATED BY FLORENSIA (122040013)
### DATA TYPES ###
# Make sure you note these differences
a1 = 1 == 1.0  # True
a2 = 1 == '1'  # False

# Comparing characters according to their LEXICOGRAPHICAL ORDER (ASCII Table for further info)
a4 = 'a' < 'b'  # True
a5 = 'a' < 'A'  # False
a6 = 'abd' < 'aca'  # True

# check the data type
b1 = type('1')  # <class 'str'>
b2 = type(10)  # <class 'int'>
x = True
b3 = type(x)  # <class 'bool'>
b4 = type(1.2)  # <class 'float'>

# Data type conversion
c1 = int(9.8)  # 9
c2 = str(123)  # '123'
c3 = int('10.4')  # ERROR because it is a float string
c3 = int(10.4)  # 10
c4 = float('10.4')  # 10.4
c4 = float('10')  # 10.0

### PRINT FUNCTION ###
# print(b2)  # value = b2

# sep: separator (what separator you want to use between two print values)  --> MUST BE A STRING!
# end: ending (what ending you want to use when the print statement is done) --> MUST BE STRING!
# print(b1, b2, a1, sep=';', end=' end print function')
# print(b1, b2, a1, sep=';', end='\n')
# print(b1, b2, a1, sep=';')

# print('%s hello' % b2)

# for any string, integer or floating numbers
# print('%5s' % 'hey')
# print('%-5s' % 'hey')
# print('%-5smiau' % 'hey')
# print('%5s' % 'heyloo')
# print('%-5s' % 'heyloo')

# ONLY FOR FLOATING NUMBERS
# print('%-5.3f' % 0.123)
# print('%5.2f' % 0.125)
# print('%-10.2f hey' % (12.345))


### ARITHMETIC OPERATORS ###
# for numeric values
number_operations1 = 9 % 5
number_operations2 = 2 ** 3
number_operations3 = 9 // 5

# For string values
string_operations1 = 'a'+'is a cat'  # 'aisacat'
string_operations2 = 'a' * 3  # 'aaa'
string_operations3 = '12' * 3  # '121212'
string_operations4 = int('12') * 3  # 36

# slice operator
st = 'crocodile'
string_operations5 = st[3]  # 'c'
string_operations6 = st[8]  # 'e'
# string_operations7 = st[9]  # ERROR
string_operations8 = st[-2]  # 'l' --> count from the back

# slice range operator
string_operations9 = st[0:5]  # 'croco'
string_operations10 = st[0:5:2]  # 'coo'
string_operations11 = st[::-1]  # 'elidocorc'

string_operations12 = st[:9]  # 'crocodile'
string_operations13 = st[:6]  # 'crocod'  -> it starts from the beginning until the fifth index
string_operations14 = st[2:]  # 'ocodile'  -> it starts from the second index until the ending

### INPUT FUNCTION ###
input_function1 = input()  # the program will request a user input
input_function2 = input("Hey, enter a number: ") 
# ^the program will request a user input but it will request by printing "Hey, enter a number: "
# REMEMBER! the default format for input is STRING
input_function3 = int(input())  # convert the user input into an integer


### EVAL FUNCTION ###
# eval() --> it helps evaluate a python STRING argument. Example: '5*3' not 5*3
# number i)
'''
a = 1
b = 3
c = 'a+b'
d = eval('a+b')  # a + b
print(c)
print(d)
'''

# number ii)
'''
a = 2
aa = 4
aaa = 8
b = eval('a+aa')  # a+aa
print(b)
'''

### PRACTICE QUESTIONS ###
# Question 1 - Print a table
'''
print('%-8s%-8s%-8s' % ('a', 'b', 'a ** b'))
print('%-8d%-8d%-8d' % (1, 2, 1 ** 2))
print('%-8d%-8d%-8d' % (2, 3, 2 ** 3))
print('%-8d%-8d%-8d' % (3, 4, 3 ** 4))
print('%-8d%-8d%-8d' % (4, 5, 4 ** 5))
print('%-8d%-8d%-8d' % (5, 6, 5 ** 6))
'''

# Question 2 - Convert Celcius to Fahrenheit
'''
celcius = int(input("Enter a degree in celcius: "))
fahrenheit = (9 * c)/5 + 32
print("Celcius degree %d equals to Fahrenheit degree %.1f." % (celcius, fahrenheit))
'''

# Question 3 - Compute the Volume
'''
radius = int(input("Enter radius for the cylinder:"))
length = int(input("Enter length for the cylinder:"))
area = radius * radius * (3.141592)
volume = area * length
print("The area is:%.2f" % area)
print("The volume is:%.2f" % volume)
'''

# Question 4 - Sum the Digits
'''
n = int(input("Enter a number between 0 and 1000: "))
sum = 0
sum += n % 10  # n%10 -> we get first digit (932%10 = 2) sum = 2
n = n // 10  # 932/10 = 93.2 -> 93 (because of the floor function)
sum += n % 10  # 93%10 = 3; sum = 2+3 = 5
n = n // 10  # 93//10 = 9
sum += n % 10  # 9 -> 9  # sum = 5 + 9 = 14
print("Sum up all the digits as:", sum)  # Sum up all the digits as: 14
'''

# Question 5 - Number of Years and Days
'''
minutes = int(input("Enter the number of minutes:"))
hours = minutes/60  # we get the number of hours
days = hours/24  # we get the number of days
num_of_years = days/365  # we get the number of days
remaining_days = days % 365  # we get the remaining days after we had done num_of_years years
print("That number will equal to %d years and %d days." % (num_of_years, remaining_days))
'''

# Question 6 - Financial Application: Compound Value
'''
monthly = int(input("Enter the monthly saving amount:$"))
r = 0.00417
total = 0
total = (total + monthly)*(1+r)  # 1st month
total = (total + monthly)*(1+r)  # 2nd month
total = (total + monthly)*(1+r)
total = (total + monthly)*(1+r)
total = (total + monthly)*(1+r)
total = (total + monthly)*(1+r)

print('After the sixth month, the acount value is:$%.2f' % total)
'''
