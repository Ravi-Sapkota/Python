import random


choices = ["scissor", "paper", "rock"]
user = input("Choose one: 'scissor', 'paper' or 'rock'\n").lower()

while user not in choices:
    user = input("Choose one form below:\n'scissor', 'paper' or 'rock'").lower()

computer = random.choice(choices)
print("Choice of computer is: " + computer)

if user == "scissor":
    if computer == "scissor":
        print("Draw")
    elif computer == "paper":
        print("Win")
    else:
        print("Loss")
elif user == "paper":
    if computer == "scissor":
        print("Loss")
    elif computer == "paper":
        print("Draw")
    else:
        print("Win")
else:
    if computer == "scissor":
        print("Win")
    elif computer == "paper":
        print("Loss")
    else:
        print("Draw")
