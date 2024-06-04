def isSorted(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True

def main():
    lst=input("Enter elements in a list separated by space:\n").split()
    lst=[eval(x) for x in lst]
    if isSorted(lst):
        print("The list is already sorted.")
    else:
        print("The list is not sorted.")

main()
