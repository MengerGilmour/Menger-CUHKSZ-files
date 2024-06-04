class Account:
    def __init__(self,ID=0,balance=100,annualInterestRate=0):
        self.__ID=ID
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate
    def setId(self,ID=0):
        self.__ID=ID
    def setBalance(self,balance=0):
        self.__balance=balance
    def setAnnualInterestRate(self,annualInterestRate=0):
        self.__annualInterestRate=annualInterestRate
    def getId(self):
        return self.__ID
    def getBalance(self):
        return self.__balance
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def getMonthlyInterestRate(self):
        MonthlyInterestRate=self.__annualInterestRate/12
        return MonthlyInterestRate
    def getMonthlyInterest(self):
        MonthlyInterest=self.__balance*self.getMonthlyInterestRate()/100
        return MonthlyInterest
    def withdraw(self,ammount=0):
        self.__balance=self.__balance-ammount
    def deposit(self,ammount=0):
        self.__balance=self.__balance+ammount

