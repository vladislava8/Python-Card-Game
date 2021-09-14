#**********************  Assigment #8.py  *********************
#
# Name: Vladislava Sicicorez
#
# Course: CSCI 1470
#
# Assignment: #8
#
# Algorithm:
#
# Import random library for random function.
# Create empty dictionary for card deck
# Define function game
# Create list of cards for Player 1 and Player 2
# Add Player 1 cards to card deck dictionary
# Define function for game processing inside game function
# Select random card for Player 1
# Select random card for Player 2
# Compare cards values to find the winner (if any e.g. tie game) referring to dictionary that will remain constant throughout the game proccess
# Delete “used” card from players card list
# Award winner 1 point
# Call game processing function inside game function
# Output and compare final scores
# Find winner
# Output winner (if any e.g. Tie)
# Call game function
# Ask user to play another game
# Call game function or exit program
#**********************************************************

import random
global cardsPlayer1
global cardsPlayer2
global deck
deck = {}

def game():
    global player1_score
    global player2_score
    cardsPlayer1 = ["two","three","four","five","six", "seven", "eight", "nine", "ten","jack","queen","king","ace"]
    cardsPlayer2 = ["two","three","four","five","six", "seven", "eight", "nine", "ten","jack","queen","king","ace"]
    player1_score = 0
    player2_score = 0
    for i in cardsPlayer1:
        deck[i] = cardsPlayer1.index(i)
    i = 0
    global j
    j = 1
    def Battle():
        global j
        print("Round {}".format(j))
        print ("*"* 25)
        print ("*"* 25)
        global player1_score
        global player2_score
        Player1_card = random.randint(0,len(cardsPlayer1)-1)
        Player2_card = random.randint(0,len(cardsPlayer2)-1)
        print ("Player 1 draw {}".format(cardsPlayer1[Player1_card]))
        print ("Player 2 draw {}".format (cardsPlayer2[Player2_card]))
        if (deck[cardsPlayer1[Player1_card]] > deck[cardsPlayer2[Player2_card]]):
            player1_score = player1_score+1
            print ("{} is bigger than {}".format(cardsPlayer1[Player1_card], cardsPlayer2[Player2_card]))
            print ("Player 1 won this round")
            print ("-"*25)
        elif(deck[cardsPlayer1[Player1_card]] < deck[cardsPlayer2[Player2_card]]):
            player2_score= player2_score +1
            print ("{} is less than {}".format(cardsPlayer1[Player1_card], cardsPlayer2[Player2_card]))
            print ("Player 2 won this round")
            print ("-"*25)
        else:
            print ("{} is equal {}".format(cardsPlayer1[Player1_card], cardsPlayer2[Player2_card]))
            print ("Tie")
            print ("No points awarded this round")
            print ("-"*25)
        print("Player 1 score: ",player1_score)
        print("Player 2 score: ",player2_score)
        print ("-"*25)
        cardsPlayer1.pop(Player1_card)
        cardsPlayer2.pop(Player2_card)
        print ("Player 1 cards left: ", cardsPlayer1)
        print ("Player 2 cards left: ", cardsPlayer2)
        j+=1
        print ("*"* 25)
        print ("*"* 25)

    for i in range(len(cardsPlayer1)):
        Battle()

    print ("Final scores:")
    print ("Player 1 Final Score: {}".format(player1_score))
    print ("Player 2 Final Score: {}".format(player2_score))
    if player1_score > player2_score:
        print ("Player 1 won!")
        print (" ♥ ♦ ♣ ♠ ")
    elif player1_score < player2_score:
        print ("Player 2 won!")
        print (" ♥ ♦ ♣ ♠ ")
    elif player1_score == player2_score:
        print ("Friendship won!")
        print (" ♥ ♦ ♣ ♠ ")
game()
print()
def cont_decision():
    print ('Would you like to play another game?')
    print ("Enter: Y/N")
    game_cont = input()
    while game_cont == "Y" or game_cont == "y":
        game()
        print ('Would you like to play another game?')
        print ("Enter: Y/N")
        game_cont = input()
    if game_cont == "N" or game_cont == "n":
        print ("Good Bye")
    else:
        print ("Wrong Entry, try again")
        cont_decision()

cont_decision()
