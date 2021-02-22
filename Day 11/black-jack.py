import art
import random
import os
clear = lambda: os.system('cls')
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def finishGame(playerCards, computerCards):
    playerScore = sum(playerCards)
    computerScore = sum(computerCards)

    while (computerScore < 16):
        computerCards.append(random.choice(cards))
        computerScore = sum(computerCards)
    print(f'''  Your final hand: {playerCards}, final score: {playerScore}
  Computer's final hand: {computerCards}, final score: {computerScore}''')
    if (computerScore > 21):
        print("The computer went bust. You win!")
    elif (playerScore > 21):
        print("You went bust. You lose!")
    elif (isPlayerCloser(playerScore, computerScore)):
        print("You were closer to 21. You win!")
    elif (not isPlayerCloser(playerScore, computerScore)):
        print("The computer was closer to 21. You lose!")

def isPlayerCloser(playerScore, computerScore):
    if ((21 - playerScore) > (21 - computerScore)):
        return False
    else:
        return True

def blackjack():
    clear()
    print(art.logo)
    playerCards = [random.choice(cards), random.choice(cards)]
    computerCards = [random.choice(cards), random.choice(cards)]
    round(playerCards, computerCards)

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        blackjack()

def round(playerCards, computerCards):
    playerScore = sum(playerCards)
    if (playerScore > 21):
        finishGame(playerCards, computerCards)
        return

    print(f'''  Your cards: {playerCards}, current score: {playerScore}
  Computer's first card: {computerCards[0]}''')
    roundContinue = input("Type 'y' to get another card, type 'n' to pass: ")
    if (roundContinue == 'y'):
        playerCards.append(random.choice(cards))
        round(playerCards, computerCards)
    elif (roundContinue == 'n'):
        finishGame(playerCards, computerCards)
        return

if input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'n':
    exit()

blackjack()
