import random

board = [1, 1, 2, 2, 3, 4, 5, 6]

balance = 0


def financial_eligibility():
    global balance  # Declare balance as a global variable
    if balance > -100:
        darts()
    else:
        print("You've already lost Rs. 100.")


def betting_choice():
    choice = int(
        input("1. Sums less than 7\n2. Sums 7\n3. Sums more than 7\nYour choice: ")
    )
    if choice > 3 or choice < 1:
        return betting_choice()
    return choice


def win_condition(bet, total_sum):
    global balance  # Declare balance as a global variable
    if bet == 1 and total_sum < 7:
        print("Congratulations you won.")
        balance = balance + 20
    elif bet == 2 and total_sum == 7:
        print("Congratulations you won.")
        balance = balance + 40
    elif bet == 3 and total_sum > 7:
        print("Congratulations you won.")
        balance = balance + 20
    else:
        print("Sorry you've lost.")
        balance = balance - 20
    print("Your new balance is {}".format(balance))
    play_again = input("Do you want to play again? [y/n]\n").lower()
    if play_again == "y":
        financial_eligibility()


def darts():
    bet = betting_choice()
    d1 = random.choice(board)
    d2 = random.choice(board)
    d3 = random.choice(board)
    print("Your dart 1 hit the number {}".format(d1))
    print("Your dart 2 hit the number {}".format(d2))
    print("Your dart 3 hit the number {}".format(d3))
    total_sum = d1 + d2 + d3
    print("Your sum is {}".format(total_sum))
    win_condition(bet, total_sum)


print("You get 3 darts to hit on a board with numbers: 1-6.")
print("You need to bet on whether you'll sum up to (less than 7, 7, or more than 7)")
print("If you bet on 7 and win, then you'll win twice the money of your entry fee.")
print("If you bet on others and win, then you'll win the same money as your entry fee.")
print("If you don't make up to your bet, you'll lose your money.\n")
print("Entry fee = 20:")

financial_eligibility()
print(f"You have exited the game.\nYour final balance is {balance}.")
