import os
import art

clear = lambda:os.system('cls')
print(art.logo)
bidders = {}
continueFlag = "yes"

while (continueFlag == 'yes'):
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    continueFlag = input("Are there any more bidders? Type 'yes' or 'no': ")
    if (continueFlag == 'yes'):
        clear()

highestBid = ["No one", 0]
for key in bidders:
    if bidders[key] > highest[1]:
        highestBid[0] = key
        highestBid[1] = bidders[key]

print(f"The winner is {highestBid[0]} with a bid of ${highestBid[1]}.")
