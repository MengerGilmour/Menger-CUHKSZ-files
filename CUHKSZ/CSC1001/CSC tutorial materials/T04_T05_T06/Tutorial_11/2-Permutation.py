#uses a loop to move a character from s2 to s1 and
#recursively invokes it with a new s1 and s2.
#The base case is that s2 is empty and prints s1 to the console.
def displayPermutationHelper(s1,s2):
    if s2 is "":
        print(s1)
    else:
        for i in s2:
            index=s2.index(i)
            displayPermutationHelper(s1+i,s2[:index]+s2[index+1:])

def displayPermutation(s):
    displayPermutationHelper("",s)

def main():
    s=input("Enter a string:")
    displayPermutation(s)

main()
        
