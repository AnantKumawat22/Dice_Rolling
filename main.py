import random


print("Rules of Dice rolling Game :-")
print("->Double Press Enter to roll the dice.")
print("->Enter x to exit.")
input("")
input("")

while(True):
    rand = random.randint(1,6)
    if(rand == 1):
        print(" __________")
        print("|          |")
        print("|          |")
        print("|     o    |")
        print("|          |")
        print("|__________|")

    elif(rand == 2):
        print(" __________")
        print("|     o    |")
        print("|          |")
        print("|          |")
        print("|     o    |")
        print("|__________|")

    elif(rand == 3):
        print(" __________")
        print("|     o    |")
        print("|          |")
        print("|          |")
        print("| o      o |")
        print("|__________|")

    elif(rand == 4):
        print(" __________")
        print("| o      o |")
        print("|          |")
        print("|          |")
        print("| o      o |")
        print("|__________|")

    elif(rand == 5):
        print(" __________")
        print("| o      o |")
        print("|          |")
        print("|     o    |")
        print("| o      o |")
        print("|__________|")

    elif(rand == 6):
        print(" __________")
        print("| o      o |")
        print("|          |")
        print("| o      o |")
        print("| o      o |")
        print("|__________|")
    ch = input("")
    if(ch == 'x'):
        break
print("Game End.")