import art
import os
clear = lambda: os.system('cls')

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculator():
    print(art.logo)
    n1 = float(input("What's the first number?: "))

    #shouldContinue = True
    while (True):
        n2 = float(input("What's the next number?: "))
        operation = input("Pick an operation: ")
        answer = operationDict[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")
        n1 = answer

        result = input(f"Type 'y' to continue calculating with {n1}, or type 'n' to start a new calculation: ")
        if result == 'n':
            clear()
            calculator()

operationDict = {
"+":add,
"-":sub,
"*":mult,
"/":div,
}

calculator()
