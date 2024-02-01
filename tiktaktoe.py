player = ["X", "O"]
chart = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
used = []


def win_condition():
    if chart[0] == chart[1] == chart[2] and chart[0].isalpha():
        print(f"{chart[0]} wins the match")
        return True
    if chart[3] == chart[4] == chart[5] and chart[4].isalpha():
        print(f"{chart[4]} wins the match")
        return True
    if chart[6] == chart[7] == chart[8] and chart[8].isalpha():
        print(f"{chart[8]} wins the match")
        return True
    if chart[0] == chart[3] == chart[6] and chart[0].isalpha():
        print(f"{chart[0]} wins the match")
        return True
    if chart[1] == chart[4] == chart[7] and chart[4].isalpha():
        print(f"{chart[4]} wins the match")
        return True
    if chart[2] == chart[5] == chart[8] and chart[8].isalpha():
        print(f"{chart[8]} wins the match")
        return True
    if chart[0] == chart[4] == chart[8] and chart[4].isalpha():
        print(f"{chart[4]} wins the match")
        return True
    if chart[2] == chart[4] == chart[6] and chart[4].isalpha():
        print(f"{chart[4]} wins the match")
        return True


def get_position():
    index = int(input("Choose the position [1-9]: "))
    while index > 9 or index < 1:
        print(f"Your position {index} is invalid.")
        return get_position()
    while index in used:
        print(f"You have already value({index}).")
        return get_position()
    used.append(index)
    print(f"You have used: {used}")
    return index


def display():
    i = 0
    for ch in chart:
        i = i + 1
        if i % 3:
            print(ch, end=" | ")
        else:
            print(ch)


def tiktaktoe():
    i = 1
    while i < 10:
        print(f"It is {player[i%2]}'s turn:")
        position = get_position()
        chart[position - 1] = player[i % 2]
        display()
        if win_condition() == True:
            break
        i = i + 1


tiktaktoe()
