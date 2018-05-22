import tkitner as *
import random
import final as *

#All Pseudo coding, need text-based project file to integrate and compromise

win_Total = 0
loss_Total = 0
#set screen to display main menu first
screen = 1


root = Tk.tk()

#Define all frames
scoreFrame = Frame(root, side = LEFT)
gameFrame = Frame(root)
optionsFrame = Frame(root, side = BOTTOM)

scoreFrame.pack()
gameFrame.pack()
optionsFrame.pack()


#Scores for all wins and loss

def win_Score(win_Tally):
	win_Total = win_Total + win_Round
def loss_Score(loss_Tally):
	win_Total = win_Total + win_Round

#Text for labeling
win_Text = Label(scoreFrame, text = "wins:", sticky = E)
loss_Text = Label(scoreFrame, text = "wins:", sticky = E)

#Counting score text
win_Tally = Label(scoreFrame, fg = "red")
loss_Tally = Label(scoreFrame, fg = "red")

#Arranged for display
win_Text.grid(row = 0)
win_Tally.grid(row = 0, column = 1)
loss_Text.grid(row = 1)
loss_Tally.grid(row = 1, column = 1)


#All Player input in given lines

#screen = 1 | Main Menu
question = Label(optionsFrame, text = "Select Gamemode")
rpsButton = Button(optionsFrame, text = "RPS", fg = "red")
diceButton = Button(optionsFrame, text = "Dice", fg = "purple")
cardsButton = Button(optionsFrame, text = "Cards", fg = "green")

#screen = 2 | RPS
rockButton = Button(optionsFrame, text = "Rock", fg = "red")
paperButton = Button(optionsFrame, text = "Paper", fg = "purple")
scissorsButton = Button(optionsFrame, text = "Scissor", fg = "green")

#screen = 3 | Dice
question = Label(optionsFrame, text = "How Many Sides Will the Dice Have?")
amount = Entry(optionsFrame)
submitButton = Button(optionsFrame, text = "Submit")

#screen = 4 | Cards
yes_Shuffle = Button(optionsFrame, text = "Yes", fg = "red")
no_Shuffle = Button(optionsFrame, text = "No", fg = "blue")

left_Side = Button(optionsFrame, text = "Left", fg = "red")
middle_Side = Button(optionsFrame, text = "Middle", fg = "blue")
right_Side = Button(optionsFrame, text = "Right", fg = "green")

#screen = 5 | End of Game
statement = Label(optionsFrame, text = "Game Over")
continueButton = Button(optionsFrame, text = "Continue", fg = "red")
changeButton = Button(optionsFrame, text = "Change Gamemode", fg = "blue")

def input_change(mode):
	while screen > 0:
		if mode == "none":
			question.pack()
			rpsButton.pack()
			diceButton.pack(side = LEFT)
			cardsButton.pack(side = LEFT)

			if screen != 1:
				question.pack_forget()
				rpsButton.pack_forget()
				diceButton.pack_forget()
				cardsButton.pack_forget()

		if screen == 2:
			rockButton.pack()
			paperButton.pack(side = LEFT)
			scissorButton.pack(side = LEFT)

			if screen != 2:
				rockButton.pack_forget()
				paperButton.pack_forget()
				scissorButton.pack_forget()

		if screen == 3:
			question.pack()
			amount.grid(row = 0)
			submitButton.pack()

			if screen != 3:
				question.pack_forget()
				amount.grid_forget()
				submitButton.pack_forget()

		if screen == 4:
			yes_Shuffle.pack()
			no_Shuffle.pack(side = LEFT)

			if shuffle == "No":
				yes_Shuffle.pack_forget()
				no_Shuffle.pack_forget()
				left_Side.pack()
				middle_Side.pack(side = LEFT)
				right_Side.pack(side = LEFT)

			if screen != 4:
				yes_Shuffle.pack_forget()
				no_Shuffle.pack_forget()
				left_Side.pack_forget()
				middle_Side.pack_forget()
				right_Side.pack_forget()

		if screen == 5:
			statement.pack()
			continueButton.pack()
			changeButton.pack(side = LEFT)

			if screen != 5:
				statement.pack_forget()
				continueButton.pack_forget()
				changeButton.pack_forget()


root.mainloop()
