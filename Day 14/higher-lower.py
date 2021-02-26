import art
import game_data
import random
import os

clear = lambda: os.system('cls')

def formatChoices(A, B):
    for i in [A, B]:
        if i['country'] == "United State":
            i['country'] = "the United States"

def higherLower(score, prev, lose):
    clear()
    print(art.logo)

    if (lose):
        print(f"Sorry, that's wrong. Final score: {score}")
        return

    A = prev
    B = random.choice(game_data.data)
    formatChoices(A, B)

    if (score != 0):
        print(f"You're right! Current score: {score}")

    print(f'''Compare A: {A['name']}, a {A['description'].lower()} from {A['country']}
    {art.vs}
Against B: {B['name']}, a {B['description'].lower()} from {B['country']}''')

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if (A['follower_count'] > B['follower_count']):
        answer = "A"
    else:
        answer = "B"

    if (choice == answer):
        higherLower(score + 1, B, False)
    else:
        higherLower(score, B, True)

higherLower(0, random.choice(game_data.data), False)
