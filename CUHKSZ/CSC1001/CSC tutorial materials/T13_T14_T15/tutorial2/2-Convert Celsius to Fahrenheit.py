##Prompt up the indicator for users to enter degree in Celsius
celsius=eval(input("Enter a degree in Celsius:"))

##Convert the celsius degree into Fahrenheit degree
fahrenheit=(9/5)*celsius+32

##Displace the result,change the sep equal to nothing '' instead of the default value with one space ' '
print("Celsius degree ",celsius," equals to Fahrenheit degree ",fahrenheit,".",sep='')
