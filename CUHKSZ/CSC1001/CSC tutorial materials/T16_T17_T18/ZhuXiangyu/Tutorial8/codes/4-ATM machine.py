##As long as your program doesn't stop, the information stored won't miss.

from Accountclass import Account

def main():
##  Store those IDs that already are registered in the bank
    idList=[0,1,2,3,4,5,6,7,8,9]
##  Create an Account class for each ID
    accountList=[Account(ID) for ID in idList]
    while True:
        yourId=eval(input('Enter your ID:'))
        if yourId not in idList:
            print('Please enter a correct ID.')
        else:
##          Select the account corresponding to the ID that the user inputs
            account=accountList[idList.index(yourId)]
            while True:
                print('-'*20)
                print('Main menu')
                print('1:check balance')
                print('2:withdraw')
                print('3:deposit')
                print('4:exit')
                print('-'*20)
                choice=eval(input('Enter a choice:'))
                if choice==4:
                    print('Good Bye!')
                    break
                elif choice==1:
                    print('The balance is',account.getBalance())
                elif choice==2:
                    amount=eval(input('Enter an amount to withdraw:'))
                    account.withdraw(amount)
                elif choice==3:
                    amount=eval(input('Enter an amount to deposit:'))
                    account.deposit(amount)
            print('\n')

main()
