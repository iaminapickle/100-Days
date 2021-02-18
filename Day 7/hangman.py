import random
import hangman_art
import hangman_words

def printWord(correctCount):
    for letter in word:
        if (letter == guess or letter in guessedLetters):
            print(f"{letter} ", end = "")
            correctCount += 1
        else:
            print(f"_ ", end = "")
    print("\n")
    print(hangman_art.stages[lives])

def checkWin():
    finishLen = len(set(word))
    if (correctCount == finishLen):
        return 1
    else:
        return 0


lives = 6

word = random.choice(hangman_words.word_list)
guessedLetters = []
correctCount = 0

print(hangman_art.logo)
print(word)
while (not checkWin() and lives != 0):

    guess = input("Guess a letter: ")

    if guess in guessedLetters:
        print("This letter has already been guessed!")
    else:
        guessedLetters.append(guess)
        if guess not in word:
            print(f"You guessed {guess} incorrectly! You lose a life.")
            lives -= 1
        printWord(correctCount)

if (lives == 0):
    print("You lose!")
else:
    print("You win!")
