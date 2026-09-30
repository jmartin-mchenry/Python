"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. RESPONSES is a tuple containing at least 8 string options.
[X] 3. Program uses a 'while True' loop to keep the game running.
[X] 4. random.choice() selects the answer from the tuple.
[X] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later", "Likely so", "Likely not", "I don't know", "You can answer that yourself")

print("Welcome to the Digital Oracle!")

# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop

while True:
    question = input("Enter your yes or no question (quit to quit): ")
    question = question.strip().lower()

    # imo using "in" is too loose, as the user's question could contain the word "quit",
    # even if the user does not want to quit the application.
    if "quit" in question:
        break

    # random.choice chooses an element from a sequence
    # https://docs.python.org/3/library/random.html#random.choice
    response = random.choice(RESPONSES)

    print(f"The magic 8 ball says: {response}")
