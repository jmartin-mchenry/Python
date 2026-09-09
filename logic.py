"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter a second integer: "))

if num1 > 0 and num2 > 0:
    print("num1 and num2 are both greater than zero")

if num1 > 100 and num2 > 100:
    print("num1 and num2 are both greater than 100")

if num1 % 2 == 0 or num2 % 2 == 0:
    print("num1 and/or num2 is even")

if num1 < 100 or num2 < 100:
    print("num1 and/or num2 is less than 100")

if not num1 == num2: # could use != but assignment requires usage of the not keyword
    print("num1 is not equal to num2")

if num1 > 0:
    print("num1 is positive")
elif num1 < 0:
    print("num1 is negative")
else:
    # We don't need to check num1 == 0, since checking if it's greater or less than zero should cover all other cases,
    # (Note: we would still need to check if num1 == 0 if it was a float, since floats can be NaN. However, num1 is an int)
    print("num1 is zero")
