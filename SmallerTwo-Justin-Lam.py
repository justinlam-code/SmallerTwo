# Programmer: Justin Lam
# Jan 20th 2022
# Course: ICS201
# Fourth implementation of card game
# Features : Limit the amount of play
#          : Score added for winner

# import the random variable
# to allow for the shuffling of the deck
# and to preserve the random aspect
# of a real card game

import random

# main function
# to better organize
# the code
def main():

    # shuffle function
    # to allow for the "deck" to be shuffled
    # automatically whenever called
    # so there is no need for further action

    def shuffle(deck):
        random.shuffle(deck)
        return deck

    # these are the mapped values
    # in order for the card comparison to work
    # I had to create two variables (or four)
    # 2 for the comparison and 2 for the output values

    mapSuits = ["\u2662", "\u2663", "\u2665", "\u2664"]
    mapRanks = [3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2]

    # this is the deck function
    # this creates the deck
    def buildDeck():
        # empty deck list so we can
        # reference deck
        deck = []

        # these are the values used for later
        # comparison
        suits = [0, 1, 2, 3]
        ranks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # Here we assign the rank and suit
        # to the var currentVal in the format
        # stated below where rank is first
        # and suit is second
        # when suit is in suits and rank
        # is ranks, the card val will equal
        # the rank, suit, and then it will
        # add currentVal to the afromentioned
        # "deck"
        for suit in suits:
            for rank in ranks:
                currentVal = [rank, suit]
                deck.append(currentVal)
        return deck

    # This is getting the cards
    # and then allowing for in the event of a rule change
    # for the players to draw the cards again 
    def getCards(numCards, bigDeck):
        cardsDrawn = []
        for x in range(numCards):
            cardsDrawn.append(bigDeck.pop(0))
        return cardsDrawn

    # This is the showHand function to litteraly
    # Show the hand of the player
    # in the format of rank then suit
    def showHand(player, playerHand):
        print("[ Player {} ".format(player + 1), "]")
        print("[ Your hand is ]")
        # this part of the code allows for the user
        # to input a number to choose what card they
        # are playing
        y = 1
        for card in playerHand:
            # here are where the mapped values come in to play
            # to display a better representation of the deck
            print("{}) {} {}".format(y, mapRanks[card[0]], mapSuits[card[1]]))
            # when the cards move down the list, the number beside it
            # to make the card choice will increase by 1 as it goes down
            y += 1

    # this determines if the card chosen by the player is allowed
    # to be played in reference to standard big 2 rules
    def canPlay(suit, rank, playerHand):
       # checking the card in playerHand
        for card in playerHand:
            # when card[0] being rank which is the first of the list
            # it will return true

            # rank = [0] as it is first in the list and python
            # starts lists off at zero
            if card[0] > rank:
                return True
            if card[0] == rank:

                # card[1] is the suit of the "card"
                # if current card is greater
                # than the card to beat suit
                # it will return true
                if card[1] > suit:
                    return True

        # if the card being chosen does not follow
        # these "parameters" it will return false
        # making it so the player can't play the card
        return False

    # Initializing variables here as it is after
    # the buildDeck and shuffle var are assigned

    bigDeck = buildDeck()
    bigDeck = shuffle(bigDeck)
    remove = []
    players = []

    def Game():
        # prints a game title and asks the user how many players will be playing
        print("[[[[((( BIG 2 )))]]]]")
        numPlayers = (input("[ How many players are going to be playing? ] :"))

        # in order for no traceback errors I was forced to use the isnumeric method to check
        # if the numPlayers input was an integer, as putting just int front of the input
        # would make it so strings would output an error, discovering alterative ways to
        # require a integer response became neccessary.

        # if the int response does not fit in between 2 or 4 it will result in an invalid popup
        # as my big 2 version does not support more than 4 players, and having less than 2 players
        # would be illogical.
        while (not numPlayers.isnumeric()) or int(numPlayers) < 2 or int(numPlayers) > 4:
            numPlayers = (input("[ Invalid response: please input a number that is in between (2 to 4) ] :"))
        # re-assinging that numPlayers is an integer
        numPlayers = int(numPlayers)

        # this for loop takes the num of players and will distribute 13 cards to each of the players
        # in a case of 3 players the deck it will still distribute 13 cards as it is not dividing
        # the deck by the numPlayers but just distributing 13 cards from the deck, leaving the len of
        # the deck in a 3 person scenario to 39

        for player in range(numPlayers):
            players.append(getCards(13, bigDeck))





        # assinging the variables

        # turn of the player set to 0 (first person)
        playerTurn = 0

        # player with the last card
        lastcardPlayer = -1

        # setting playing to default true as we want
        # to play the game
        playing = True

        # the current suit is -1 as a python list starts at 0
        # so to get the value where the state of the var is null
        # it would be negative 1
        currentSuit = -1
        currentVal = -1

        # passing equals false at default and will be change to when
        # the user inputs that they would like to pass
        passing = False

        while playing:
            # first shows of the hand of teh player with the current control
            showHand(playerTurn, players[playerTurn])

            # this is setting the card to beat of bassically playing the card input
            # if I were to play a 3 of diamonds it would check if current(x) is still null
            # and if its not(!=) it would print the card I played and the card to beat
            if currentVal != -1 and currentSuit != -1:
                print("Card to beat {} {}".format(mapRanks[currentVal], mapSuits[currentSuit]))

            # this just checks if the whole table is null
            # if every one is at a state of null where they can't play a card
            # or the voluntearly passed it would go back to the last player who had
            # the card played

            if passing and lastcardPlayer == playerTurn:
                passing = False
                currentVal = -1
                currentSuit = -1
                lastcardPlayer = -1
                print("[Whole table passed, its back to you]")

            # Checks length of the player hand
            # if hand is null than the game will end
            if len(players[playerTurn]) == 0:
                playing = False
                winner = ("Player {}".format(playerTurn + 1))

            # if it is not playing anymore than
            # it will output a congratulations message
            if playing == False:
                print("[Game Over]")
                print("[Congrats the winner is :", winner, "]")

            # if the user canPlay then this condition will activate
            if canPlay(currentSuit, currentVal, players[playerTurn]):

                cardChosen = input("[Which card do you want to play? Input 'pass' to pass your turn] :")

                # this makes it so that if user volutaraly passes it will pass
                if not (lastcardPlayer != -1 and cardChosen == "pass"):

                    # if you are the first player you cannot pass
                    # this will prompt an invalid response for any misunderstandings
                    # from the user
                    
                    while (lastcardPlayer == -1 and cardChosen == "pass") or not canPlay(currentSuit, currentVal, [players[playerTurn][int(cardChosen) - 1]]):
                        cardChosen = input("[Invalid response: Which card do you want to play?] :")
                    # makes it so that the chosen card response from the user is an integer
                    # as the choice is an integer next to the mapped values
                    cardChosen = int(cardChosen)
                    
                    # displays the card chosen by the user
                    print("[ You played {} {}]".format(mapRanks[players[playerTurn][cardChosen - 1][0]], mapSuits[players[playerTurn][cardChosen - 1][1]]))
                    
                    # reassigns the variables 
                    currentSuit = players[playerTurn][cardChosen - 1][1]
                    currentVal = players[playerTurn][cardChosen - 1][0]
                    lastcardPlayer = playerTurn

                    # this removes the played card from the deck
                    # pop is used to remove an item from a list
                    # and in this case it will remove the chosen card
                    # from said list
                    remove.append(players[playerTurn].pop(cardChosen - 1))

                # if else, will pass the turn
                else:
                    print("You passed your turn")
                    passing = True

            # if the user cannot play a card it will activate this else condition
            # prompting that you have passed your turn
            else:
                print("[ You can't play, you are forced to pass ]")
                passing = True
            playerTurn = (playerTurn + 1) % numPlayers

        # create a score aspect of the game
        # will print out winner and score
        if playing == False:

            # Score set to 0 to start
            # As the more players win the score goes up by 1
            playerScore = 0
            playerScore = (playerScore+ 1)

            # prints the winner of the game
            print("[ The winner is  ", winner, "with", playerScore, "points")

            # Asks if they want to play again
            again = input("[Do you want to play again? Y/N] :")

            # If score exceeds 10 game will end
            # Speciel limit to combat gambiling addiction
            if playerScore > 10:
                print("Score exceeds 10, please take a break, the game will now end")
                playing == False

            # If the input is a number it will prompt an invalid input
            if again.isnumeric():
                again = input("[Invalid Input : Do you want to play again?] : ")
            again = str(again)
            if again.upper() == "Y":
                playing = True
                Game()

    Game()
main()
