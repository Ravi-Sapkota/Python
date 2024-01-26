import random

board = [1, 2, 3, 4, 5, 6]


def betting_choice():
    choice = int(input("1. Sums less than 7\n2. Sums 7\n3. Sums more than 7"))
    if choice > 3 or choice < 1:
        betting_choice()
    return choice


def win_condition(bet, sum):
    if bet == 1 and sum < 7:
        print("Congratulations you won.")
        balance = balance + 20
        print("Your balance is now {}".format(balance))
    elif bet == 2 and sum == 7:
        print("Congratulations you won.")
        balance = balance + 40
    elif bet == 3 and sum > 7:
        print("Congratulations you won.")
        balance = balance + 20
    else:
        print("Sorry you've lost.")
    print("Your new balance is {}".format(balance))
    playagain = input("Do you want to play again?[y/n]").lower()
    if playagain == "y":
        darts()


def darts():
    balance = balance - 20
    bet = betting_choice()
    d1 = random.choice(board)
    d2 = random.choice(board)
    d3 = random.choice(board)
    print("Your dart 1 hit the number {}".format(d1))
    print("Your dart 2 hit the number {}".format(d2))
    print("Your dart 3 hit the number {}".format(d3))
    sum = d1 + d2 + d3
    print("Your sum is {}".format(sum))
    win_condition(sum, bet)


balance = 0
print("You get 3 darts to hit on a board with numbers: 1-6.")
print("You need to bet on wheather you'll sum up to (less than 7, 7 or more than 7)")
print("If you bet on 7 and win then you'll win twice the money of your entry fee.")
print("If you bet on others and win then you'll win the same money of your entry fee.")
print("If you don't make up to your bet, you'll lose your money.\n")
print("Entry fee = 20:")

darts()
print(f"You have exited the game.\nYour final balance is {balance}.")
