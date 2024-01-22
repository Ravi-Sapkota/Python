import time
import winsound


def unit_test():
    flag = int(input("1. Hour\n2. Minute\n3. Second\n"))
    if flag > 0 and flag < 4:
        return flag
    print("WRONG INPUT, enter the correct choice this time:")
    unit_test()


def second_conversion():
    print("\a")
    choice = unit_test()
    t = int(input("Enter the time: "))
    if choice == 1:
        t = t * 3600
    elif choice == 2:
        t = t * 60
    return t


print("Choose the unit of time:")
time.sleep(second_conversion())

for i in range(6):
    winsound.Beep(440, 500)
