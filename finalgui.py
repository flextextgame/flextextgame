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



root.mainloop()
