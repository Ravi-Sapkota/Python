player = ["X", "O"]
chart = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
used = []


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
        i = i + 1


tiktaktoe()
