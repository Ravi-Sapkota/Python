import time

start_time = time.perf_counter()
no_of_word = 1
original_text = "a quick brown fox jumps over the lazy dog"

input_text = input(f"Enter the text\n{original_text}\n")
end_time = time.perf_counter()

if original_text == input_text:
    for ch in input_text:
        if ch == " ":
            no_of_word = no_of_word + 1
else:
    print("Your text doesn't match with given text.")
    exit(0)


elapsed_time = end_time - start_time
print(
    f"No of words : {no_of_word}\nTime taken : {elapsed_time:.2f}\nWPM = {no_of_word/elapsed_time*60:.2f}"
)
