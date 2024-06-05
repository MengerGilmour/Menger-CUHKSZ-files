from Queue import ListQueue
from Customer import Customer
from Server import Server
from arrivalTime import arrivalTime
from math import exp
from random import random

#timUnit=0.1second
timeUnit=0.1

#How many units are there in 1min
NumUnit=int(60/timeUnit)

#Total times(mins)
totalTime=120
totalTime*=NumUnit
    
class Simulation:
    def __init__(self,lamda,mu,totalTime):
        #Parameters supplied by the user
        self.__lamda=lamda
        self.__mu=mu
        self.__totalTime=totalTime
        #Simulation components
        self.__CustomerQ=ListQueue()
        #Computed during the simulation
        self.__totalWaitTime=0
        self.__numCustomers=0
        
    #Run the simulation using the parameters supplied earlier
    def run(self):
        self.server=Server()
        self.idNum=1
        for curTime in range(self.__totalTime+1):
            self.__handleArrival(curTime)
            self.__handleBeginService(curTime)
            self.__handleEndService(curTime)
##            print('current time:',curTime)                                            #####①print
##            print(self.__CustomerQ)

    #get the average waiting time of each customer
    def getaverageWaitTime(self):
        numServed=self.__numCustomers-len(self.__CustomerQ)
        return float(self.__totalWaitTime/NumUnit)/numServed

    #get the length of customer in queue
    def getlenQueue(self):
        return len(self.__CustomerQ)
        
    #Print the simulation results
    def printResults(self):
        numServed=self.__numCustomers-len(self.__CustomerQ)
        avgWait=float(self.__totalWaitTime/NumUnit)/numServed
        print("Total number of customers=",self.__numCustomers)
        print("Number of customers served=",numServed)
        print("Number of customers remaining in line=%d"%len(self.__CustomerQ))
        print("The average wait time was %4.2f mins."%avgWait)
    
    def __handleArrival(self,curTime):
        if curTime==0:
            self.arTime=arrivalTime(self.__lamda,timeUnit)
            #To store the time when previous customer arrives
            self.customerarTime=0
##            print('arTime:',self.arTime,'current time:',curTime)                       #####②print
        else:
            if curTime==self.customerarTime+self.arTime:
                c=Customer(self.idNum,curTime)
                self.__CustomerQ.enqueue(c)
                self.__numCustomers+=1
                self.idNum+=1
                self.customerarTime=curTime
                self.arTime=arrivalTime(self.__lamda,timeUnit)
##                print('arTime:',self.arTime,'current time:',curTime)                   #####③print
        
    def __handleBeginService(self,curTime):
        if not self.__CustomerQ.is_empty() and self.server.getservedCustomer()==None:
            customer=self.__CustomerQ.first()
            #Begin to serve the first arrival customer when he arrives
            if customer.getidNum()==1:
                if curTime==customer.getarrivalTime():
                    #Generate the service time for the first arrival
                    self.serTime=arrivalTime(self.__mu,timeUnit)
##                    print('serTime:',self.serTime,'current time:',curTime)            #####④print
                    self.server.startService(customer,curTime+self.serTime)
            else:
                self.server.startService(customer,curTime+self.serTime)
            
    def __handleEndService(self,curTime):
        if curTime==self.server.getstopTime():
            customer=self.server.stopService()
            self.serTime=arrivalTime(self.__mu,timeUnit)
##            print('serTime:',self.serTime,'current time:',curTime)                    #####⑥print
            #Waiting time is the time after served-the time he comes??
            self.__totalWaitTime+=curTime-customer.getarrivalTime()
            self.__CustomerQ.dequeue()


# ###①test to look at the queue for at every time, uncomment the 6 print functions at #①~⑥print
# ###timUnit=1second
# timeUnit=1
# totalTime=30
# simulation=Simulation(9,10,totalTime)
# simulation.run()
# simulation.printResults()


# #②test--to find out the length of queue after a long time, and average waiting time for each customer
# def main():
#     simulation=Simulation(9,10,totalTime)
#     simulation.run()
#     simulation.printResults()

# main()


###③test--to run for many times and average the length of queue and average waiting time, to compare with the theoretical result L=9, WT=0.9mins
##def main():
##    averageLenQueue=0
##    averageWaitTime=0
##    numSimulation=1000
##    for i in range(numSimulation):
##        simulation=Simulation(9,10,totalTime)
##        simulation.run()
##        averageLenQueue+=simulation.getlenQueue()
##        averageWaitTime+=simulation.getaverageWaitTime()
##    averageLenQueue/=numSimulation
##    averageWaitTime/=numSimulation
##    print('Average Length of Queue:',averageLenQueue)
##    print('Average Waiting Time for each customer:',averageWaitTime)
##
##main()

