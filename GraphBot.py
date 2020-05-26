from Graphics import Graphics
from Graphics import HEIGHT
from Graphics import WIDTH

#You may modify colors here
BOT='purple'
POISON='red'
FOOD='green'
EMPTY='grey'
WALL='black'

#Next abstraction after Graphics.py.

class BotGraphics:
    def __init__(self):                #Generate new field
        self.gui=Graphics()
        self.gui.update()

    def newBot(self,x,y,counter):              #Put a new bot to field
        self.gui.change_color(x,y,BOT)
        self.setText(x,y,counter)

    def destroy(self,x,y):              #Change cell to empty
        self.gui.change_color(x,y,EMPTY)
        self.removeText(x,y)

    def moveBot(self,xinit,yinit,xfinal,yfinal,counter):              #Delete bot(text/color) from initial position and set to final position
        self.gui.change_color(xfinal,yfinal,BOT)
        self.gui.change_color(xinit, yinit, EMPTY)
        self.removeText(xinit, yinit)
        self.setText(xfinal, yfinal,counter)

    def setFood(self,x,y):              #Put a new food to field
        self.gui.change_color(x,y,FOOD)

    def setPoison(self,x,y):              #Put a new poison to field
        self.gui.change_color(x,y,POISON)
    def setWall(self,x,y):
        self.gui.change_color(x, y, WALL)


    def setText(self,x,y,text):              #Puts text to a cell
        self.gui.change_text(x,y,text)

    def removeText(self,x,y):              #Delete any text from cell
        self.gui.change_text(x,y,"")
    def update(self):
        self.gui.update()
    def test(self):
        self.logic.test()
    def setStat(self,index,text):
        self.gui.change_text(WIDTH, index, text)