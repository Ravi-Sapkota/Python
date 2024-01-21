import random

x = 10
y = 100
a = random.randint(x, y)
b = int(input("Guess a number between {} and {}: ".format(x, y)))
count = 1

while b < x or b > y:
    b = int(input("Please guess a number between {} and {}: ".format(x, y)))
    count += 1


while a != b:
    count += 1
    if b < a:
        b = int(input("Try a larger number: "))
    else:
        b = int(input("Try a smaller number: "))

print(
    "Congratulations you have sucessfully found the number({}) in {} attemps.".format(
        a, count
    )
)
