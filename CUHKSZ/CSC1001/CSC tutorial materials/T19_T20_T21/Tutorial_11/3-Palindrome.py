def check(string):
    if string=='':
        return True
    elif string[0]==string[len(string)-1] and check(string[1:len(string)-1]):
        return True
    else:
        return False

def main():
    string=input('Enter a string:')
    print(check(string))

main()
