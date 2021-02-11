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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(choiceList[choice])

print("Computer chose:\n")
compChoice = random.randint(0,2)
print(choiceList[compChoice])

compBeats = (compChoice + 1) % 3
if (compBeats == choice):
    print("Win!")
elif (compChoice == choice):
    print("Tie!")
else:
    print("Loss!")