from tkinter import *
import random

#All Pseudo coding, need text-based project file to integrate and compromise

win_Total = 0
loss_Total = 0
#set screen to display main menu first
screen = 1


root = Tk()

#Define all frames
scoreFrame = Frame(root)
gameFrame = Frame(root)
playerFrame = Frame(root)

#left side
scoreFrame.pack(side=LEFT)
#right-top side
gameFrame.pack()
#right-bottom side
playerFrame.pack()

#score frame on left
wins = Label(scoreFrame, text = "Wins:", fg = "red")
wins.grid(row = 0)
win_Total = Label(scoreFrame, text = "0", fg = "blue")
win_Total.grid(row = 0, column = 1)
loss = Label(scoreFrame, text = "Loss:", fg = "red")
loss.grid(row = 1)
loss_Total = Label(scoreFrame, text = "0", fg = "blue")
loss_Total.grid(row = 1, column = 1)

#player input frame
#when mode is "none"
rpsButton = Button(playerFrame, text = "RPS", fg = "red")
diceButton = Button(playerFrame, text = "Dice", fg = "red")
cardsButton = Button(playerFrame, text = "Cards", fg = "red")

rpsButton.pack(side=LEFT)
diceButton.pack(side=LEFT)
cardsButton.pack(side=LEFT)
    
root.mainloop()
