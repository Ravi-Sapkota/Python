def win_condition():
    return 0


def display_figure():
    i = 0
    for value in value_dict.values():
        i = i + 1
        if i % 3:
            print(value, end=" | ")
        else:
            print(value)


value_dict = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

turn = ["X", "O"]
turn_selector = 1
print("Choose position as: ")
for key in value_dict:
    if key % 3:
        print(key, end=" ")
    else:
        print(key)

while not win_condition() and turn_selector < 10:
    mark = turn[turn_selector % 2]
    print("It is {}'s turn.".format(mark))
    position = int(input("Choose the index of position as above: "))
    value_dict[position] = mark
    turn_selector = turn_selector + 1
    display_figure()
