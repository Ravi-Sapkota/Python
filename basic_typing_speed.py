import time
import random


result_list = []
text_list = [
    "pack my box with five dozen liquor jugs",
    "a quick brown fox jumps over the lazy dog",
    "how razorback jumping frogs can level six piqued gymnasts",
    "sphinx of black quartz judge my vow",
    "the five boxing wizards jump quickly",
]


def final_results():
    total_speed = sum(result_list)
    no_of_runs = len(result_list)
    average = total_speed / no_of_runs
    print(f"Your average speed for {no_of_runs} runs is {average:.2f} WPM.")


def results(words, time):
    speed = words / time * 60
    print(f"\n\nWords = {words}\nTime Taken = {time:.2f} sec\nSpeed(WPM) = {speed:.2f}")
    result_list.append(speed)
    try_again = input("Give it another try?[y/n]").lower()
    if try_again == "y":
        speed_testing()
    else:
        final_results()


def speed_testing():
    no_of_word = 1
    original_text = random.choice(text_list)
    for ch in original_text:
        if ch == " ":
            no_of_word = no_of_word + 1
    start_time = time.perf_counter()
    input_text = input(f"Rewrite the text below\n{original_text}\n")
    end_time = time.perf_counter()
    if original_text == input_text:
        results(no_of_word, end_time - start_time)
    else:
        print("Your input text doesn't match.")


speed_testing()
