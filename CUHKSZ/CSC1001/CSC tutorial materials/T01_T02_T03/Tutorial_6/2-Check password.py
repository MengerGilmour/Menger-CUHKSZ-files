##Define a function to check whether the password is valid
def isValidPassword(password):
    if len(password)<8:             
        print("A password must have at least eight characters.")
        return False
    if not password.isalnum():
        print("A password must consist of only letters and digits.")
        return False
    count=0
    for ch in password:
        if ch.isdigit():
            count+=1
    if count<2:
        print("A password must contain at least two digits.")
        return False
    else:
        return True

##Define a main function to keep inputting a password until it is valid
def main():
    while True:
        password=input("Please enter a password:")
        if isValidPassword(password):
            print("The password is valid.")
            break
        else:
            print("Sorry!The password is invalid.Please enter again!")

main()
