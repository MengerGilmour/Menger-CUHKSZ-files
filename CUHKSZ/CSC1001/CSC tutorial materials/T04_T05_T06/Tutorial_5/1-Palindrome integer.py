####Using numeric operators to define reverse function
##def reverse(number):
##    reverseNumber=0
##    while number != 0:          
##        remainder=number%10
##        reverseNumber=reverseNumber*10+remainder
##        number//=10
##    return reverseNumber

##Using string to define reverse function
def reverse(number):
    reverseNumber=''
    while number != 0:
        reverseNumber+=str(number%10)
        number//=10
    reverseNumber=int(reverseNumber)
    return reverseNumber

##Define a function to judge whether a number is palindrome or not    
def isPalindrome(number):
    if number==reverse(number):
        return True
    else:
        return False

##Define a main function to input an integer and display whether it is a palindrome
def main():
    num=eval(input("Enter an integer:"))
    if isPalindrome(num):
        print("%d is a palindrome."%num)
    else:
        print("%d is not a palindrome."%num)

main()
