import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choiceList = [rock, paper, scissors]

userChoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if userChoice not in [0, 1, 2]:
    print("You typed an invalid number! You lose!")
    exit()
userChoice = int(userChoice)
print(choiceList[userChoice])

compChoice = random.randint(0,2)
print(f"Computer chose: {compChoice}\n")
print(choiceList[compChoice])

compBeats = (compChoice + 1) % 3
if (compBeats == userChoice):
    print("Win!")
elif (compChoice == userChoice):
    print("Tie!")
else:
    print("Loss!")
