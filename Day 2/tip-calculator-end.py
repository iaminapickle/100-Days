print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
no = int(input("How many people to split the bill? "))

cost = round((total * (1 + percentage/100)) / no, 2)

print(f"Each person should play: ${cost}")
