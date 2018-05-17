import random
# Title: Flex-Text game

"""
Objective: Beat the CPU (Computer) in either of the three random number
generator game. Wins and loss for each game are accumulated.
RPS: Rock, Paper, Scissor | Select either of the three choices
        Win conditions:
        Rock > Scissor
        Paper > Rock
        Scissor > Paper
Dice: Roll the dice (only get to choose the amount of sides the dice has)
        Win condition: Get a higher value than the CPU
Cards: Select a card from the shuffled deck
        Win condition: Get a higher value than the CPU
        Card to Number defitnion:
        Ace = 1
        Jack = 11
        Queen = 12
        King = 13
Note: every "print('\n')" is creating extra blank lines to space out texts
"""


#Mode to "none" indicating Parent to run
mode = "none"

#initial Total win/loss tallied
win_total = 0
loss_total = 0

#Parent of all gamemodes 
while mode == "none":
        #Reset round win/loss
        win = 0
        loss = 0

        #print total win/loss under the following conditions
        if win_total > 0:
                print("Total Win: " + win_total)
        if loss_total > 0:
                print("Total loss: " + loss_total)

        #Menu: asks player to choose either of the three gamemodes
        mode = input("RPS, Dice, or Cards: ")

        #Input from Menu converted to lowercase | accomodates for any uppercase string
        mode = mode.lower()

        #loop for any input not favorable to Menu
        if mode != "rps":
                if mode != "dice":
                        if mode != "cards":
                                mode = "none"
                                continue

        print('\n')

        #Rock Paper Scissor | change if Menu receives "rps"
        while mode == "rps":

                #set Rounds to 0 for counting
                rounds = 0

                #3 rounds to loop count | function of gamemode begins
                while rounds < 3:
                        
                        #Player chooses the three options
                        player_choice = input("Rock, Paper, or Scissor: ")

                        #goes back to player_choice if Input does not meet
                        if player_choice != "rock":
                                if player_choice != "paper":
                                        if player_choice != "scissor":
                                                player_choice = "none"
                                                continue
                        #makes player_choice lowercase for string comparison in win/loss/tie conditions
                        player_choice = player_choice.lower()
                        
                        print('\n')

                        #print player_choice
                        print("Player: " + player_choice)
                        
                        #Computer's choice
                        cpu = random.randint(1, 3)
                        #convert integers to nouns
                        if cpu == 1:
                                cpu = "rock"
                        if cpu == 2:
                                cpu = "paper"
                        if cpu == 3:
                                cpu = "scissor"
                        #print Computer's choice
                        print("Computer: " + cpu)

                        print('\n')

                        #win/loss/tie conditions for each of the three choices
                        if player_choice == "rock":
                                if cpu == "rock":
                                        print("Tie")
                                if cpu == "paper":
                                        loss = loss + 1
                                        print("You Lose")
                                if cpu == "scissor":
                                        win = win + 1
                                        print("You Win")	
                        if player_choice == "paper":
                                if cpu == "paper":
                                        print("Tie")
                                if cpu == "scissor":
                                        loss = loss + 1
                                        print("You Lose")
                                if cpu == "rock":
                                        win = win + 1
                                        print("You Win")
                        if player_choice == "scissor":
                                if cpu == "scissor":
                                        print("Tie")
                                if cpu == "rock":
                                        loss = loss + 1
                                        print("You Lose")
                                if cpu == "paper":
                                        win = win + 1
                                        print("You Win")

                        #print total wins and loss in each round
                        print("Wins: " + str(win))
                        print("Loss: " + str(loss))

                        print('\n')

                        #count rounds to limit loop of gamemode
                        rounds = rounds + 1

                #continue or change mode
                continue_mode = input("Continue [1] or Change Mode [2]: ")
                #Option to continue
                if continue_mode == "1":
                    continue
                #Option to change gamemode
                else:
                    #tally up wins and loss of the rounds and add to Total win/loss
                    win_total = win_total + win
                    loss_total = loss_total + loss
                    #change Mode to return to Menu
                    mode = "none"


        #Dice Rolling Game
        while mode == "dice":

                #rounds initially set to 0
                rounds = 0

                #Game begins for 3 rounds
                while rounds < 3:
                    #set roll to 0
                    player_roll = 0

                    #Player choose the amount of sides on the dice
                    dice_sides = input("How many sides do you want the dice to have [above 2]: ")

                    #checks if dice_sides input is an integer
                    try:
                        dice_sides = int(dice_sides)
                    #loops back to dice_sides if dice_sides is not an integer
                    except ValueError:
                            continue
                    #loops back to dice_sides if input is 2 or below (impossible shape)
                    if dice_sides <= 2:
                            print("Must be above 2")
                            print("-"*30)
                            continue

                    #begins to roll and receive a side
                    player_roll = random.randint(1, dice_sides)

                    #CPU roll set to 0
                    cpu_roll = 0
                    #CPU begins to roll and receive a side using the input as the range
                    cpu_roll = random.randint(1, dice_sides)

                    print('\n')

                    #print the sides rolled from both Player and CPU
                    print("Player: " + str(player_roll))
                    print("CPU: " + str(cpu_roll))

                    #win/loss/tie conditions with comparative operations 
                    if player_roll > cpu_roll:
                            win = win + 1
                            print("You Win")
                    elif player_roll < cpu_roll:
                            loss = loss + 1
                            print("You Lose")
                    else:
                            print("Tie")

                    #print total wins and loss for each round
                    print("Wins: " + str(win))
                    print("Loss: " + str(loss))
                    
                    print('\n')

                    #count rounds to limit loop
                    rounds = rounds + 1

                #continue or change mode
                continue_mode = input("Continue [1] or Change Mode [2]: ")
                #Option to continue
                if continue_mode == "1":
                    continue
                #Option to change gamemode
                else:
                    #tally up wins and loss and transfer to Total wins/loss
                    win_total = win_total + win
                    loss_total = loss_total + loss
                    #change Mode to return to Menu
                    mode = "none"
                    

        #Card Game
        while mode == "cards":

                #initially set rounds to 0
                rounds = 0

                #begin game for 3 rounds
                while rounds < 3:
                        
                        #set shuffle option to *blank*                                  
                        shuffle = ""
                        #shuffling error state set to 0
                        shuffle_error = 0
                        #loop shuffle when *blank*
                        while shuffle == "":
                                #13 cards defined in deck
                                deck = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
                                #deck multiplied to get full deck
                                deck = deck * 4
                                #shuffled deck set blank
                                
                                #keeps previous shuffled_deck if error in shuffle permission occurs
                                if shuffle_error == 0:
                                        shuffled_deck = []
                                        #begin shuffling for 52 times
                                        for i in range(52):
                                                shuffled_deck.append(random.choice(deck))
                                                deck.remove(shuffled_deck[i])                                        
                                if shuffle_error == 1:
                                        shuffled_deck == shuffled_deck
                                                                      
                                print('\n')

                                #ask Player if they want to shuffle deck again
                                shuffle = input("Do you want to shuffle the deck [Yes or No]: ")
                                #makes sure all alphabets are lowercase for string comparison
                                shuffle = shuffle.lower()
                                #shuffle again if input is "yes"
                                if shuffle == "yes":
                                        print('\n')
                                        shuffle = ""
                                        shuffle_error = 0
                                        continue
                                #loops to asking to shuffle again if answer is neither "yes" or "no"
                                if shuffle != "no":
                                        shuffle_error = 1
                                        shuffle = ""
                                        print("Must be either of the two options in square brackets.")
                                        print('\n')
                                        continue                                

                        #CPU selects a card from shuffled_deck
                        cpu_select = random.choice(shuffled_deck)

                        print('\n')
                        
                        #resets what Player input is for the side they pick (refer to below for details)
                        pick_side = ""
                        #ask Player to pick a side from shuffled_deck when spread out in imaginary hands
                        while pick_side == "":
                                print('\n')
                                pick_side = input("Pick a side to pick from [left, middle, right]: ")
                                #makes sure text-based input is applicable for string comparison
                                pick_side = pick_side.lower()
                                #loops to side picking if either of the three choices aren't met
                                if pick_side != "left":
                                        if pick_side != "middle":
                                                if pick_side != "right":
                                                        pick_side = ""
                                                        continue
                                #if Player picked the left side
                                if pick_side == "left":
                                        #cards from the furthest left to the right until the 18th card
                                        select_deck = shuffled_deck[:18]
                                        #asks Player to select a card from the given range inputed
                                        card_select = input("There are 18 cards. Pick one [1 to 18]: ")
                                        #makes sure input is the correct type
                                        try:
                                                card_select = int(card_select)
                                        #loop to side picking if input's type is incorrect
                                        except ValueError:
                                                pick_side = ""
                                                continue
                                        card_select = card_select - 1
                                        
                                #if Player picked the middle side
                                if pick_side == "middle":
                                        #asks Player to select a card from the 18 cards in the middle section (9 from the left to 9 from the right)
                                        select_deck = shuffled_deck[16:34]                                    
                                        #asks Player to select a card from the given range inputed
                                        card_select = input("There are 18 cards. Pick one [1 to 18]: ")
                                        #makes sure input is the correct type
                                        try:
                                                card_select = int(card_select)
                                        #loop to side picking if input's type is incorrect
                                        except ValueError:
                                                pick_side = ""
                                                continue
                                        card_select = card_select - 1
                                #if Player picked the right side        
                                if pick_side == "right":
                                        #asks Player to select a card from the furthest right to the left until the 18th card
                                        select_deck = shuffled_deck[34:]                                        
                                        #asks Player to select a card from the given range inputed
                                        card_select = input("There are 18 cards. Pick one [1 to 18]: ")
                                        #makes sure input is the correct type
                                        try:
                                                card_select = int(card_select)
                                        #loop to side picking if input's type is incorrect
                                        except ValueError:
                                                pick_side = ""
                                                continue
                                        #accomodates for index as the 1st card is at position 0
                                        card_select = card_select - 1
                                #select card according to Player's input
                                player_select = select_deck[card_select]=

                        #Print cards selected by both Player and CPU
                        print("Player: " + str(player_select))
                        print("CPU: " + str(cpu_select))

                        #Player: card string translation
                        if player_select == "Ace":
                                player_select = 1
                        if player_select == "Jack":
                                player_select = 11
                        if player_select == "Queen":
                                player_select = 12
                        if player_select == "King":
                                player_select = 13

                        #CPU: card string translation
                        if cpu_select == "Ace":
                                cpu_select = 1
                        if cpu_select == "Jack":
                                cpu_select = 11
                        if cpu_select == "Queen":
                                cpu_select = 12
                        if cpu_select == "King":
                                cpu_select = 13

                        #Player win/loss/tie print conditions
                        if player_select > cpu_select:
                                print("You Win")
                                win = win + 1
                        elif player_select < cpu_select:
                                print("You Lose")
                                loss = loss + 1
                        else:
                                print("Tie")

                        #prints win/loss statistics of the round
                        print("Wins: " + str(win))
                        print("Loss: " + str(loss))

                        #count rounds to limit loop of gamemode
                        rounds = rounds + 1

                        print('\n')

                #asks Player to continue or change gamemode
                continue_mode = input("Continue [1] or Change Mode [2]: ")
                #option to continue gamemode
                if continue_mode == "1":
                        #makes sure shuffled_deck is shuffled for new rounds of gamemode
                    shuffle_error = 0
                    print('\n')
                    continue
                #option to switch gamemode
                else:
                    #tally up wins and loss of the rounds and add to Total win/l
                    win_total = win_total + win
                    loss_total = loss_total + loss
                    print('\n')
                    #switch text to Menu
                    mode = "none"        
