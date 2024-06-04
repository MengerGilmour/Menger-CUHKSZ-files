def prefix(s1,s2):
    i=0
    s=s1[i]
    while i<len(s1) and s2.startswith(s):
##      Enlarge the prefix untill it is not common
        i+=1
##      Slicing the string to get prefix
        s=s1[:i+1]             
    s=s1[:i]  # i=0 will produce empty string
    return s

def main():
    s1=input("Enter the first string:")
    s2=input("Enter the second string:")
    print("The longest common prefix of the two strings is \"",prefix(s1,s2),"\".",sep="")

main()
