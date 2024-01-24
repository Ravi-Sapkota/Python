import random

dictionary = {
    "earth": "A planet",
    "jupiter": "A planet",
    "mercury": "A planet",
    "satrun": "A planet",
    "uranus": "A planet",
    "elephant": "A mammal",
    "whale": "A mammal",
    "giraffe": "A mammal",
    "monkey": "A mammal",
    "rabbit": "A mammal",
    "republicofkorea": "A county",
    "afghanistan": "A county",
    "france": "A county",
    "mozambique": "A county",
    "southsudan": "A county",
    "munamadan": "A movie",
    "kusumerumal": "A movie",
    "nainabhannula": "A movie",
    "hamitinbhai": "A movie",
    "hostelreturns": "A movie",
    "rhythm": "Repeted pattern of sound",
}


def get_key():
    return random.choice(list(dictionary.items()))


def display(key, guessed):
    on_screen = ""
    for ch in key:
        if ch in guessed:
            on_screen += ch
        else:
            on_screen += "*"
    return on_screen


def hangman():
    attemps = 7
    guessed = []
    key, value = get_key()
    print("Welcome to hangman game!!")
    print("Hint : " + value)

    while attemps > 0:
        ch = input("\nChoose a character: ")
        if ch in key:
            print("Your guess is correct.")
            guessed += ch
        else:
            print("Your guess is wrong.")
            attemps = attemps - 1
        print(f"Attemps left = {attemps}")
        print(display(key, guessed))
        if len(set(key)) == len(set(guessed)):
            return True
    if attemps == 0:
        print("Your word was '{}'".format(key))


game = hangman()
print("\n" * 3)
if game == True:
    print("You Won")
else:
    print("You lost")
