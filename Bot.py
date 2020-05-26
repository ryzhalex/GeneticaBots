import random
MAX_Pointer=40
COUNTER=5
MAXENERGY=100


# This class describes one bot. Currently bot has coordinates, energy, and genom


class Bot:
    def __init__(self,X,Y,index):

        self.x=X
        self.y=Y
        self.alive=True
        self.genom = []
        self.energy=50
        self.move=15
        self.pointer=0
        self.counter=COUNTER
        self.index=index
        self.randomGenom()
    def getIndex(self):
        return self.index

    def getGenom(self):
        return self.genom
    def getEnergy(self):
        return self.energy
    def addEnergy(self,points):
        if self.energy+points> MAXENERGY:
            self.energy=MAXENERGY
        else:
            self.energy+=points
    def kill(self):
        self.alive=False
    def isAlive(self):
        return self.alive
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
         self.x=x
    def setY(self,y):
        self.y =y
    def resetMoves(self):
        self.move = 15
    def increasepointer(self,i):
        if self.pointer+i>=MAX_Pointer-1:
            self.pointer=i-(MAX_Pointer-1-self.pointer)
        else:
            self.pointer+=i
    def resetPointer(self):
        self.pointer=0
    def jumpPointer(self,destination):
        self.pointer=destination
    def resetCounter(self):
        self.counter=COUNTER
    def getCounter(self):
        return self.counter
    def randomGenom(self):
        for i in range(MAX_Pointer):
            self.genom.append(random.randint(0,MAX_Pointer-1))



    def action(self):
        self.counter-=1
        self.energy-=1
        print(self.pointer)
        return self.genom[self.pointer]


