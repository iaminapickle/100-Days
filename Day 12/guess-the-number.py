import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5

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
