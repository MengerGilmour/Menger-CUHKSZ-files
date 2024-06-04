def conv(n,base):
    if n//base==0:
        print(n,end='')
    else:
        conv(n//base,base)
        print(n%base,end='')
        
print('In binary system，12=')
conv(12,2)    #should be 1100
print()
print('In octal system，20=')
conv(20,8)    #should be 24
