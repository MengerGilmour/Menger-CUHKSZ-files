def findSubset(L,T):
    if len(L)==0:
        return [] 
    for i in range(len(L)):
        subset=list()
        for element in L:
            if element !=L[i]:
                #Find all the possible true subsets with only one element excluded
                subset.append(element)
        if subset not in T:
            findSubset(subset,T)
            T.append(subset)
    return T

L=[1,2,3]
Output=findSubset(L,[])
print(Output)
