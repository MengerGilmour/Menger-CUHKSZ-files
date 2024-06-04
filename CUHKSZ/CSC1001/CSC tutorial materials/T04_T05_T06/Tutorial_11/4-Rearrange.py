def rearrange(lst):
    if len(lst)==0:
        return []
    #If the first element is odd,rearrange the sublist after this element,
    #and then insert it to position at the end of all even numbers,
    #to avoid changing the original order of odd numbers.
    elif lst[0]%2==1:
        L0=lst[0]
        lst=rearrange(lst[1:len(lst)])
        index=0
        while index<len(lst):
            if lst[index]%2==1:
                lst.insert(index,L0)
                break
            index+=1
        if index==len(lst):
            lst.insert(index,L0)
        return lst
    else:
        lst=[lst[0]]+rearrange(lst[1:len(lst)])
        return lst

def main():
    lst=[1,4,3,2]
    print(rearrange(lst))

main()
