'''##①
##Privious code for summing up the digits
##Prompt up the indicator for user to enter
number=eval(input("Enter a number between 0 and 1000:"))
##Use the variable to do the operation
sumup=0
sumup+=number%10
number//=10
sumup+=number%10
number//=10
sumup+=number%10
##Display the result
print("Sum up all the digits as:",sumup)
'''##①



'''##②
##Prompt up the indicator for user to enter
number=eval(input("Enter a number:"))
##Use sumup to store the sum of digits
sumup=0
##if number is bigger than 0, there are digits to be summed, so go into the loop
while number>0:
##  sum up the digit
    sumup+=number%10        
##  remove the digit already being summed
    number//=10              
##Display the result
print("Sum up all the digits as:",sumup)
'''##②



##③
while True:
    ##  Prompt up the indicator for user to enter
    number=eval(input("Enter a number:"))
    ##  Use sumup to store the sum of digits
    sumup=0
    ##  if number is bigger than 0, there are digits to be summed, so go into the loop
    while number>0:
        ##  sum up the digit
        sumup+=number%10
        ##  remove the digit already being summed
        number//=10
        
    ##  Display the result
    print("Sum up all the digits as:",sumup)
    
    ##  Use decision to store the string determining whether to continue or not
    decision=input("Do you want to continue? y or n:")
    ##  If you input 'y', then continue to enter a number, otherwise stop
    if decision !='y':
        break
    ##  This part can be omitted
    else:              
        continue
##③



















