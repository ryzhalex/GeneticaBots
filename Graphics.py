import tkinter as tk
import time
SLEEP=0.1
HEIGHT=20
WIDTH=40


#This is the most deep level of graphics.

#DO NOT MODIFY: TO CHANGE GRAPHICS SEE GraphBot.py

class Graphics:


    counter = 0
    def __init__(self):
        self.board = [[None] * HEIGHT for _ in range(WIDTH)]
        self.root = tk.Tk()
        self.root.geometry("1500x700")


        for i, row in enumerate(self.board):
            for j, column in enumerate(row):
                L = tk.Label(self.root, text='    ', bg='grey',height=1,width=2,borderwidth=1,relief="groove",font=("Courier", 20))
                L.grid(row=j, column=i, sticky="WENS")
                self.board[i][j]=L

        j=0
        self.board.append([])
        while(j<6):
            L = tk.Label(self.root, text='STATS', bg='White',height=2,width=10)
            L.grid(row=j, column=WIDTH+1)
            L.bind('<Button-1>', lambda e, i=j, j=WIDTH+1: self.start(e, ))
            self.board[WIDTH].append(L)
            j+=1


    def start(self,e):
        self.board[0][0].config(bg='red')

    def change_color(self,i,j,color):
        self.board[i][j].config(bg=color)
    def change_text(self,i,j,text):
        self.board[i][j].config(text=str(text))
    def loop(self):
        self.root.mainloop()
    def update(self):
        time.sleep(SLEEP)
        self.root.update()



