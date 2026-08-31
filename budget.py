"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Ask user for Monthly Income (float).
[X] 3. Ask user for 5 DIFFERENT expense amounts (float).
[X] 4. Calculate Total Expenses and Remaining Balance.
[X] 5. Calculate Percentage of Income Spent.
[X] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

income = float(input("Enter your gross monthly income: "))
housing = float(input("Enter your rent or mortage: "))
streaming = float(input("Enter the amount you spend on streaming services: "))
phone = float(input("Enter the amount you spend on your phone plan: "))
internet = float(input("Enter the amount you spend on internet: "))
other = float(input("Enter the total of any other expenses: "))

total_expense = housing + streaming + phone + internet + other
remaining_balance = income - total_expense
fraction_income_spent = total_expense / income

# Not sure how to use python's string formatting to get clean columns here... I could store stuff in temporary strings
# but that feels kinda clunky. Just spaces works I guess.
print(f"total expense:                          ${total_expense:.2f}")
print(f"remaining balance:                      ${remaining_balance:.2f}")
print(f"percentage of income spent on expenses: {fraction_income_spent:.2%}")
