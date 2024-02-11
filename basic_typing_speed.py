import time

# Start timer
start_time = time.perf_counter()
no_of_word = 1

print("Enter the text on the screen:")
text = input("\na quick brown fox jumps over the lazy dog\n")

# End timer
end_time = time.perf_counter()

for ch in text:
    if ch == " ":
        no_of_word = no_of_word + 1

# Calculate elapsed time
elapsed_time = end_time - start_time
print(
    f"No of words : {no_of_word}\nTime taken : {elapsed_time:.2f}\nWPM = {no_of_word/elapsed_time*60:.2f}"
)
