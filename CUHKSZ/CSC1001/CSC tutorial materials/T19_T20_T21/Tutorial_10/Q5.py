def fun(n):
    count = 0
    m = n//2
    for i in range(n, 0, -m):
        m=m//2
        for j in range(0, i, 1):
            print('i is %d, j is %d'%(i, j))
            count += 1
    print(count)
    return count

fun(6)
