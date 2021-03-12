#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()


prev_name = "[name]"
for name in names:
    name = name.strip()
    starting_letter = starting_letter.replace(prev_name, name)
    with open(f"Output/ReadyToSend/{name}.txt", "w") as file:
        file.write(starting_letter)
    prev_name = name
