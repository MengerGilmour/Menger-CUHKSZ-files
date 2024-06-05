class Player:
    def __init__(self,name='',score=0):
        self.name=name
        self.score=score
    def getName(self):
        return self.name
    def resetScore(self):
        self.score=0
    def increaseScore(self):
        self.score+=1
    def __str__(self):
        return str((self.name,self.score))
    def __repr__(self):
        return 'Player'+str(self)

import random
class Computer(Player):
    def __init__(self):
        super().__init__()
    def getMove(self):
        return random.randint(1,10)
    def __repr__(self):
        return 'Computer'+str(self)

class Human(Player):
    def __init__(self):
        super().__init__()
    def getMove(self):
        while True:
            try:
                n=int(input('Enter an integer:'))
                if n>=1 and n<=10:
                    return n
                else:
                    print('invalid input')
            except:
                print('invalid input')
    def __repr__(self):
        return 'Human'+str(self)

def main():
    c=Computer()
    c.name='MyPython'
    h=Human()
    h.name='Jay'
    print(playUnderCut(c,h))

def playUnderCut(p1,p2):
    p1.resetScore()
    p2.resetScore()
    m1=p1.getMove()
    m2=p2.getMove()
    if m1==m2-1:
        p1.increaseScore()
        return p1.getName()+' moves '+str(m1)+' '\
               +p2.getName()+' moves '+str(m2)+' '\
               +p1.getName()+' wins '
    elif m2==m1-1:
        p2.increaseScore()
        return p1.getName()+' moves '+str(m1)+' '\
               +p2.getName()+' moves '+str(m2)+' '\
               +p2.getName()+' wins '
    else:
        return p1.getName()+' moves '+str(m1)+' '\
               +p2.getName()+' moves '+str(m2)+' '\
               'draw: no winner'
    
main()
