import random

password_choice = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 1]
password = []
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
special = ["@", "#", "$"]
special_count = 0
for i in range(16):
    if random.choice(password_choice) == 1:
        print(random.choice(alphabet), end="")
    elif random.choice(password_choice) == 2:
        print(random.choice(alphabet).upper(), end="")
    else:
        print(random.choice(special), end="")
print()

print(len(password_choice))
