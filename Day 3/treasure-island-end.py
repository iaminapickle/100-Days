print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

leftRight = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
if (leftRight != "left"):
    print("You get attacked by 3 goblins! Game over.")
    exit()

swimWait = input("You arrive at a pier at a lake. Do you want to swim across or wait for a boat? Type \"swim\" or \"wait\"\n").lower()
if (swimWait != "wait"):
    print("A giant river snake gobbles you up midway! Game over.")
    exit()

doorColour = input("You arrive at a castle with three doors. Do you want to go in the red, blue or yellow door? Type \"red\", \"blue\" or \"yellow\"\n").lower()
if (doorColour != "yellow"):
    print("You open the door and are blasted with fire! Game over.")
    exit()

print("You open the door and are met with a magical glowing orb! You win!")
