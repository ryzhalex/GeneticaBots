from itertools import accumulate

from GraphBot import BotGraphics
from Graphics import HEIGHT
from Graphics import WIDTH
from Bot import Bot
from Mutator import Mutator
from Stats import Stats
import random

#Dont touch these parameters

EMPTY=0
FOOD=1
POISON=2
WALL=3

#You can experiment with these

BOTS=30
FOODENERGY=25

#Checks if coordinates are positive

def tryCordinates(x,y):
    if(x<0):
        return False
    if (y < 0):
        return False
    if (x >= WIDTH):
        return False
    if (y >= HEIGHT):
        return False
    return True


#Class that runs the game. TODO: SPLIT TO SMALLER CLASSES


class GameLogic:

    def __init__(self):

        #

        self.field=[]
        self.bots=[]
        self.mutator = Mutator()

        self.graphics=BotGraphics()
        self.generateMap()
        self.graphics.setStat(0, "ITERATION")
        self.graphics.setStat(2,"MOVE")
        self.graphics.setStat(4, "LAST BEST")
        self.stat=Stats()


#Building map object

    def generateMap(self):
        for i in range(WIDTH):
            line =[]
            for j in range(HEIGHT):
                line.append(EMPTY)
            self.field.append(line)

#Add given amount of food randomly to the field

    def addFood(self,times):
        for i in range(times):
            y = random.randint(0,HEIGHT-1)
            x = random.randint(0,WIDTH-1)
            self.field[x][y] = FOOD
            self.graphics.setFood(x,y)

# Add given amount of poison randomly to the field

    def addPoison(self, times):
        for i in range(times):
            y = random.randint(0, HEIGHT-1)
            x = random.randint(0, WIDTH-1)
            self.field[x][y] = POISON
            self.graphics.setPoison(x, y)

# Delete all information from square on the  map

    def remove(self,x,y):
        self.field[x][y]=EMPTY
        self.graphics.destroy(x,y)

    def newBots(self):
        for i in range(BOTS):
            y = random.randint(0, HEIGHT - 1)
            x = random.randint(0, WIDTH - 1)
            self.bots.append(Bot(x,y,i))
            self.graphics.newBot(x,y,0)
            self.graphics.update()
    def randomisePositions(self):
        for bot in self.bots:
            y = random.randint(0, HEIGHT - 1)
            x = random.randint(0, WIDTH - 1)
            bot.setX(x)
            bot.setY(y)
            self.graphics.newBot(x,y,0)
            self.graphics.update()

    def Mutate(self):
        self.bots=self.mutator.mutation(self.bots,1,1,30)
        self.randomisePositions()

    def moveBot(self,xi,yi,xf,yf,counter):

        self.graphics.moveBot(xi,yi,xf,yf,counter)
        if self.field[xi][yi]==FOOD:
            self.graphics.setFood(xi,yi)
        if self.field[xi][yi]==POISON:
            self.graphics.setPoison(xi,yi)
    def killBot(self,bot):
        bot.kill();
        self.stat.addTop(bot.getIndex())


#Run one round of simulation
#If bot doesnt eat enought or eats poison it dies

    def runRound(self):
        i=0

        while (i<50):
            deads=0
           # print(deads)
            for bot in self.bots:
                bot.resetCounter()
                #bot.resetPointer()
                while (bot.getCounter()!=0):
                    if bot.getEnergy()==0:
                        self.killBot(bot)
                    if bot.isAlive():
                        action = bot.action()
                        self.interpritate(action,bot)
                        self.graphics.setText(bot.getX(),bot.getY(),bot.getEnergy())
                        if (action > 0 and action <= 8):
                            break
                    else:
                        deads+=1
                        self.graphics.destroy(bot.getX(),bot.getY())
                        break
            if(deads==BOTS):
                self.graphics.setStat(5, self.stat.getMove())
                print("Round is done")
                break
            self.stat.addMove()
            self.graphics.setStat(1,self.stat.getMove())
            self.graphics.update()


    #Bot class returns an action code, which is interprited here

    def run(self,times):
        for i in range(0,times):
            self.runRound()
            self.Mutate()


    def interpritate(self,action,bot):
        if(action>0 and action <=8):
            self.move(action,bot)
            bot.increasepointer(1)
        if(action>8 and action <= 16):
            self.eat(action, bot)
            bot.increasepointer(1)
        if (action > 16 and action <= 24):
            self.convertPoison(action, bot)
            bot.increasepointer(1)
        if (action > 24 and action <= 32):
            self.scan(action, bot)
        if (action> 32):
            self.pointerJump(bot,action)




    #fOR EACH ACTION CODE THERE ARE INSTRUCTIONS WHAT TO DO

    def move(self,place,bot):
        if (place == 1):

                targX = bot.getX() - 1
                targY = bot.getY() - 1
                if (tryCordinates(targX, targY)):
                    X = bot.getX()
                    Y = bot.getY()
                    bot.setY(targY)
                    bot.setX(targX)

                    self.moveBot(X, Y, targX, targY, bot.getEnergy())

        if (place == 2):


                targX = bot.getX()
                targY = bot.getY() - 1
                if (tryCordinates(targX, targY)):
                    X = bot.getX()
                    Y = bot.getY()
                    bot.setY(targY)
                    bot.setX(targX)

                    self.moveBot(X, Y, targX, targY, bot.getEnergy())

        if (place == 3):


                targX = bot.getX() +1
                targY = bot.getY() - 1
                if (tryCordinates(targX, targY)):
                    X = bot.getX()
                    Y = bot.getY()
                    bot.setY(targY)
                    bot.setX(targX)

                    self.moveBot(X, Y, targX, targY, bot.getEnergy())



        if (place == 4):

                targX = bot.getX() +1
                targY = bot.getY()
                if (tryCordinates(targX, targY)):
                    X=bot.getX()
                    Y=bot.getY()
                    bot.setY(targY)
                    bot.setX(targX)

                    self.moveBot(X, Y, targX, targY, bot.getEnergy())

        if (place == 5):


                targX = bot.getX() +1
                targY = bot.getY() +1
                if (tryCordinates(targX, targY)):

                    X = bot.getX()
                    Y = bot.getY()
                    bot.setY(targY)
                    bot.setX(targX)

                    self.moveBot(X, Y, targX, targY, bot.getEnergy())



        if(place==6):



                targX = bot.getX()
                targY = bot.getY() + 1
                if (tryCordinates(targX, targY)):
                    X = bot.getX()
                    Y = bot.getY()
                    bot.setY(targY)
                    bot.setX(targX)

                    self.moveBot(X, Y, targX, targY, bot.getEnergy())


        if (place == 7):


                targX = bot.getX()-1
                targY = bot.getY() + 1
                if (tryCordinates(targX, targY)):
                    X = bot.getX()
                    Y = bot.getY()
                    bot.setY(targY)
                    bot.setX(targX)

                    self.moveBot(X, Y, targX, targY, bot.getEnergy())


        if (place == 8):


                targX = bot.getX() -1
                targY = bot.getY()

                if(tryCordinates(targX,targY)):
                    X = bot.getX()
                    Y = bot.getY()
                    bot.setY(targY)
                    bot.setX(targX)
                    self.moveBot(X, Y, targX, targY, bot.getEnergy())

    def pointerJump(self,bot,address):
        bot.jumpPointer(address)

    def eat(self,target,bot):
        if (target==9):
            targX = bot.getX()-1
            targY = bot.getY() - 1
            try:
                if(self.field[targX][targY]==FOOD):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX,targY)

                if (self.field[targX][targY] == POISON):
                    self.killBot(bot)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 10):
            targX = bot.getX()
            targY = bot.getY() - 1
            try:
                if (self.field[targX][targY] == FOOD):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)

                if (self.field[targX][targY] == POISON):
                    self.killBot(bot)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 11):
            targX = bot.getX() + 1
            targY = bot.getY() - 1
            try:
                if (self.field[targX][targY] == FOOD):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)

                if (self.field[targX][targY] == POISON):
                    self.killBot(bot)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 12):
            targX = bot.getX() + 1
            targY = bot.getY()
            try:
                if (self.field[targX][targY] == FOOD):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)

                if (self.field[targX][targY] == POISON):
                    self.killBot(bot)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 13):
            targX = bot.getX() + 1
            targY = bot.getY() + 1
            try:
                if (self.field[targX][targY] == FOOD):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)

                if (self.field[targX][targY] == POISON):
                    self.killBot(bot)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 14):
            targX = bot.getX()
            targY = bot.getY() + 1
            try:
                if (self.field[targX][targY] == FOOD):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)

                if (self.field[targX][targY] == POISON):
                    self.killBot(bot)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 15):
            targX = bot.getX() - 1
            targY = bot.getY() + 1
            try:
                if (self.field[targX][targY] == FOOD):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)

                if (self.field[targX][targY] == POISON):
                    self.killBot(bot)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 16):
            targX = bot.getX() - 1
            targY = bot.getY()
            try:
                if (self.field[targX][targY] == FOOD):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)

                if (self.field[targX][targY] == POISON):
                    self.killBot(bot)
                    self.remove(targX, targY)
            except:
                pass

    def convertPoison(self,target,bot):
        if (target == 17):
            targX = bot.getX() - 1
            targY = bot.getY() - 1
            try:
                if (self.field[targX][targY] == POISON):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 18):
            targX = bot.getX()
            targY = bot.getY() - 1
            try:
                if (self.field[targX][targY] == POISON):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 19):
            targX = bot.getX() + 1
            targY = bot.getY() - 1
            try:
                if (self.field[targX][targY] == POISON):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 20):
            targX = bot.getX() + 1
            targY = bot.getY()
            try:
                if (self.field[targX][targY] == POISON):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 21):
            targX = bot.getX() + 1
            targY = bot.getY() + 1
            try:
                if (self.field[targX][targY] == POISON):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 22):
            targX = bot.getX()
            targY = bot.getY() + 1
            try:
                if (self.field[targX][targY] == POISON):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 23):
            targX = bot.getX() - 1
            targY = bot.getY() + 1
            try:
                if (self.field[targX][targY] == POISON):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)
            except:
                pass
        if (target == 24):
            targX = bot.getX() - 1
            targY = bot.getY()
            try:
                if (self.field[targX][targY] == POISON):
                    bot.addEnergy(FOODENERGY)
                    self.remove(targX, targY)
            except:
                pass

    def scan(self,target,bot):
        if (target == 25):
            targX = bot.getX() - 1
            targY = bot.getY() - 1
            if (tryCordinates(targX, targY)):
                if (self.field[targX][targY] == POISON):
                    bot.increasepointer(2)
                if (self.field[targX][targY] == FOOD):
                    bot.increasepointer(3)
                if (self.field[targX][targY] == EMPTY):
                    bot.increasepointer(4)
                if (self.field[targX][targY] == WALL):
                    bot.increasepointer(5)

            else:
                bot.increasepointer(1)
        if (target == 26):
            targX = bot.getX()
            targY = bot.getY() - 1
            if (tryCordinates(targX, targY)):
                if (self.field[targX][targY] == POISON):
                    bot.increasepointer(2)
                if (self.field[targX][targY] == FOOD):
                    bot.increasepointer(3)
                if (self.field[targX][targY] == EMPTY):
                    bot.increasepointer(4)
                if (self.field[targX][targY] == WALL):
                    bot.increasepointer(5)

            else:
                bot.increasepointer(1)
        if (target == 27):
            targX = bot.getX() + 1
            targY = bot.getY() - 1
            if (tryCordinates(targX, targY)):
                if (self.field[targX][targY] == POISON):
                    bot.increasepointer(2)
                if (self.field[targX][targY] == FOOD):
                    bot.increasepointer(3)
                if (self.field[targX][targY] == EMPTY):
                    bot.increasepointer(4)
                if (self.field[targX][targY] == WALL):
                    bot.increasepointer(5)

            else:
                bot.increasepointer(1)
        if (target == 28):
            targX = bot.getX() + 1
            targY = bot.getY()
            if (tryCordinates(targX, targY)):
                if (self.field[targX][targY] == POISON):
                    bot.increasepointer(2)
                if (self.field[targX][targY] == FOOD):
                    bot.increasepointer(3)
                if (self.field[targX][targY] == EMPTY):
                    bot.increasepointer(4)
                if (self.field[targX][targY] == WALL):
                    bot.increasepointer(5)

            else:
                bot.increasepointer(1)
        if (target == 29):
            targX = bot.getX() + 1
            targY = bot.getY() + 1
            if (tryCordinates(targX, targY)):
                if (self.field[targX][targY] == POISON):
                    bot.increasepointer(2)
                if (self.field[targX][targY] == FOOD):
                    bot.increasepointer(3)
                if (self.field[targX][targY] == EMPTY):
                    bot.increasepointer(4)
                if (self.field[targX][targY] == WALL):
                    bot.increasepointer(5)

            else:
                bot.increasepointer(1)
        if (target == 30):
            targX = bot.getX()
            targY = bot.getY() + 1
            if (tryCordinates(targX, targY)):
                if (self.field[targX][targY] == POISON):
                    bot.increasepointer(2)
                if (self.field[targX][targY] == FOOD):
                    bot.increasepointer(3)
                if (self.field[targX][targY] == EMPTY):
                    bot.increasepointer(4)
                if (self.field[targX][targY] == WALL):
                    bot.increasepointer(5)

            else:
                bot.increasepointer(1)
        if (target == 31):
            targX = bot.getX() - 1
            targY = bot.getY() + 1
            if (tryCordinates(targX, targY)):
                if (self.field[targX][targY] == POISON):
                    bot.increasepointer(2)
                if (self.field[targX][targY] == FOOD):
                    bot.increasepointer(3)
                if (self.field[targX][targY] == EMPTY):
                    bot.increasepointer(4)
                if (self.field[targX][targY] == WALL):
                    bot.increasepointer(5)

            else:
                bot.increasepointer(1)
        if (target == 32):
            targX = bot.getX() - 1
            targY = bot.getY()
            if (tryCordinates(targX, targY)):
                if (self.field[targX][targY] == POISON):
                    bot.increasepointer(2)
                if (self.field[targX][targY] == FOOD):
                    bot.increasepointer(3)
                if (self.field[targX][targY] == EMPTY):
                    bot.increasepointer(4)
                if (self.field[targX][targY] == WALL):
                    bot.increasepointer(5)

            else:
                bot.increasepointer(1)












