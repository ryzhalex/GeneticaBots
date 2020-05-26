from Bot import Bot

class Stats:
    def __init__(self):
        self.top=[]
        self.iteration=0
        self.move=0;

    def addTop(self,index):
        self.top.append(index)

    def getFromTop(self,index):
        return self.top[index]
    def resetMoves(self):
        self.move=0

    def addMove(self):
        self.move += 1
    def getMove(self):
        return self.move
    def iteration(self):
        self.iteration+=1
