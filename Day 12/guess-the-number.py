import random

HARD_LIVES = 5
EASY_LIVES = 10


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


if difficulty == 'easy':
    lives = EASY_LIVES
elif difficulty == 'hard':
    lives = HARD_LIVES

number = random.randint(1, 100)
while (lives != 0):
    print(f"You have {lives} guesses remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high. Guess again!")
    elif guess < number:
        print("Too low. Guess again!")
    elif guess == number:
        print(f"You got it! The number was {number}")
        exit()
    lives -= 1
    if (lives == 0):
        print("You've run out of guesses, you lose!")
