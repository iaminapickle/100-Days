import art

print(art.logo)

def runCaesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(text, shift, direction)

def caesar(text, shift, direction):
    print(f"Here's the {direction}d result: ", end = "")
    for letter in text:
        if (ord(letter) < 97 or ord(letter) > 122):
            value = ord(letter)
        elif (direction == "encode"):
            if (ord(letter) + shift > 122):
                value = 96 + (ord(letter) + shift) % 122
            else:
                value = ord(letter) + shift
        elif (direction == "decode"):
            if (ord(letter) - shift < 97):
                value = 122 - (shift - ord(letter) + 96)
            else:
                value = ord(letter) - shift
        print(chr(value), end = "")
    print('\n', end = "")

continueFlag = "yes"
while (continueFlag == "yes"):
    runCaesar()
    continueFlag = input("Do you want to go again? Type 'yes' if you do, 'no' if you don't: ").lower()
