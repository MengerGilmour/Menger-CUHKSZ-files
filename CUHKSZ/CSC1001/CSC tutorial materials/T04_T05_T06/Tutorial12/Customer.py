class Customer:
    def __init__(self, idNum,curTime) -> None:
        self.idNum = idNum
        self.curTime = curTime
    
    def getidNum(self, ):
        return self.idNum
    
    def getarrivalTime(self, ):
        return self.curTime
    
    def __str__(self):
        return f"Customer {self.idNum}"