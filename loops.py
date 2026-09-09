"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[X] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

should_loop = True
while should_loop:
    response = input("Are we there yet: ")
    should_loop = response.lower() != "yes"

for i in range(99, 0, -1):
    if i == 1:
        print("1 bottle of beer on the wall!")
    else:
        print(f"{i} bottles of beer on the wall!")
