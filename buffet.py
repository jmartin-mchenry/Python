"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: 9/2/26
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)(make a variable, change to .5 if it is Tuesday)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price! (changes price calculation)
   - Sunday: Drinks are free! (print statement no change in price)
   - Other days: Standard buffet pricing in effect.
4. Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------
"""

age = int(input("Please enter your age: "))
# use .strip() to remove extra whitespace, and .lower() to convert the string to lowercase
weekday = input("Please enter the weekday: ").strip().lower()

print()

if age < 1:
    price = 0.0
elif age <= 11:
    price = age * 1.0
elif age <= 64:
    price = 16.95
else:
    price = 12.95

match weekday:
    case "tuesday" | "tue":
        print("Half off for preteens today!")
        if age <= 12:
            price /= 2.0
            print("Your drink is half off!")
        else:
            print("Not for you though, you're too old.")
    case "sunday" | "sun":
        price = 0.0
        print("Free drinks today!")
    case "monday" | "mon" | "wednesday" | "wed" | "thursday" | "thu" | "friday" | "fri" | "saturday" | "sat":
        print("No discount today.")
    # default case, see https://docs.python.org/3/tutorial/controlflow.html#tut-match
    case _:
        print("Unknown weekday, no discounts applied.")

print(f"Your final drink price: ${price:.2f}")
