from stack import ListStack

values=ListStack()

for i in range(16):
    print(values)
    if i%3==0:
        values.push(i)
    elif i%4==0:
        values.pop()
        
print(values)







