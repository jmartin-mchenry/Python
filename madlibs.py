"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[X] 1. Header Docstring included (Copy and paste THIS comment from opening to closing quotes).
[X] 2. Program asks for at least 5 different inputs (variables).
[X] 3. Output uses F-Strings to combine text and variables.
[X] 4. Output uses at least one escape sequence (\n or \t).
[X] 5. Code contains comments explaining the steps.
[X] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# Get user input, store in variables
name = input("Please enter a name: ")
adjective = input("Please enter an adjective: ")
second_adjective = input("Please enter a second adjective: ")
noun = input("Please enter a noun: ")
plural_noun = input("Please enter a plural noun: ")

# Output using f-strings and print statements
print(f"\nDid you hear? {adjective} {name} is going to be at the {noun} today! They're sure to have lots of")
print(f"{second_adjective} {plural_noun} to show off.")
