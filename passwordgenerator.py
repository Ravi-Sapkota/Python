import random

password_choice = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 1]
password_list = []
password = ""
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
for i in range(1, 16):
    if random.choice(password_choice) == 1:
        password_list.append(random.choice(alphabet))
    elif random.choice(password_choice) == 2:
        password_list.append(random.choice(alphabet).upper())
    else:
        password_list.append(random.choice(special))

for char in password_list:
    password += char

print(password)
