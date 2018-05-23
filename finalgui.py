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
optionsFrame = Frame(root)

#left side
scoreFrame.pack(side=LEFT)
#right-top side
gameFrame.pack()
#right-bottom side
optionsFrame.pack(side=BOTTOM)

wins = Label(scoreFrame, text = "Wins:", fg = "red")
wins.pack()
win_Total = Label(scoreFrame, text = "0", fg = "blue")
win_Total.pack(side = LEFT)
loss = Label(scoreFrame, text = "Loss:", fg = "red")
loss.pack(side = BOTTOM)
loss_Total = Label(scoreFrame, text = "0", fg = "blue")
loss_Total.pack(side = BOTH)

root.mainloop()
