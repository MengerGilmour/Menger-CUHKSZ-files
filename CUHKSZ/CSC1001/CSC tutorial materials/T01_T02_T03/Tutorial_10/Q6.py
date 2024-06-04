def product(n, m, count):
    if n==0:
        count+=1
        print('Count is: ', count)
        return 0
    elif n==1:
        print('Count is: ', count)
        count+=1
        return m
    else:
        if n%2==1:
            count+=1
            print('n is: ',n)
            return product(n//2, m, count)*2+m
        else:
            count+=1
            print('n is: ',n)
            return product(n//2, m, count)*2

print('Prodcut is: ',product(8,4,0))
print('Prodcut is: ',product(64,4,0))
print('Prodcut is: ',product(256,4,0))
