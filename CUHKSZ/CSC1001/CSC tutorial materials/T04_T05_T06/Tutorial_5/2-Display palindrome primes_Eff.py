import time

##Define a function to obtain the reverse of a number
def reverse(number):
    reversenumber=''
    while number != 0:
        reversenumber+=str(number%10)
        number//=10
    reversenumber=int(reversenumber)
    return reversenumber
    
##Define a function to judge whether a number is a palindrome
def isPalindrome(number):
    if number==reverse(number):
        return True
    else:
        return False

##Define a function to judge whether a number is a prime
def isPrime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    max_divisor = int(number ** 0.5) + 1
    divisor = 3
    while divisor <= max_divisor:
        if number % divisor == 0:
            return False
        divisor += 2
    return True

##Define a main function to display 100 numbers which is palindrome and prime
def main():
    count=0
    number=2                     #Begin from the smallest palindrome and prime 2
    while count<100:
        if isPalindrome(number) and isPrime(number):
            print("%6d"%number,end='')
            count+=1
            number+=1
        else:
            number+=1
            continue             #Turn to the next number if it is not what we want
        if count%10==0:          #Change line after every 10 numbers
            print()
start_time = time.time()
main()
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")