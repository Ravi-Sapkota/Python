import time

original_text = "a quick brown fox jumps over the lazy dog"


def results(words, time):
    speed = words / time * 60
    print(f"\n\nWords = {words}\nTime Taken = {time:.2f} sec\nSpeed(WPM) = {speed:.2f}")


def user_input():
    no_of_word = 1
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


user_input()
