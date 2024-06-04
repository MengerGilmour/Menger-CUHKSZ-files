##1
# nums = []
# while 1:
#     input_value = input('Enter a number: ')
#     if input_value == 'done': break
#     value = float(input_value)
#     nums += [value]
#     c = sum(nums) / len(nums)
#     print('The value of c is ', c)


##2
# lst1 = [1,2,3,4,5]
# print(len(lst1[1:-2]))
# string = "my name is x"
# print(string[1])
# for i in string.split():
#     print(i, end=", ")

# ##3
# a,b = (1,2)
# a,b = 1.2    #this assigenment is wrong
# a,b = [1,2]
# a=b=1

##4
# def question(a,b,c):
#     a = 4
#     b[1] = a**a
#     c *= a
#     print(a,',',b,',',c)
# a = 3
# b = [2,8]
# c = "9"
# question(a,b,c)
# print(a,',',b,',',c)
# #list is mutable
# #a,c is immutable

##5
# a = 2
# b = 5
# c = 9
# print(c//a+b*c%b**a)

##6
# def func(a, b=5, c=10):
#     print('a is', a, 'and b is', b, 'and c is', c)
# func(3,7)
# func(25,c=24)
# func(c=50, a=100)
