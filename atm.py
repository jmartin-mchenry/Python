"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[x] 1. Header Docstring included with assignment info.
[X] 2. ATM runs in a "while True" loop to remain awake.
[X] 3. Main menu uses match-case logic for selections.
[X] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes (include try except)
[X] 5. Logic prevents overdrafts and negative deposits.
[X] 6. All currency is formatted to two decimal places (:.2f).
[X] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

balance = 1000.0

try:
    while True:
        print("--- [ATM MENU] ---")
        print("1: View balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Transfer")
        print("5: Exit")

        choice = input("What would you like to do? [1..5]: ")

        print()

        match choice:
            case "1":
                # View balance
                print(f"Your balance: ${balance:.2f}")
            case "2":
                # Deposit
                try:
                    deposit_amount = float(
                        input("How much would you like to deposit: $"))
                    if deposit_amount > 0.0 and deposit_amount != float("inf"):
                        # If the user is allowed to deposit Infinity, they can then later deposit Infinity and
                        # end up with a NaN balance. So we disallow Infinite deposits.
                        balance += deposit_amount
                        print(f"Your new balance is ${balance:.2f}")
                    elif deposit_amount == 0.0:
                        print("No money deposited")
                    else:
                        # negative amounts, NaN
                        print("Not a valid amount of money to deposit")
                except ValueError:
                    print("Not a valid input")
            case "3":
                # Withdraw
                try:
                    withdraw_amount = float(
                        input("How much would you like to withdraw: $"))
                    if withdraw_amount > 0.0 and withdraw_amount != float("inf"):
                        if withdraw_amount > balance:
                            print(
                                "You don't have enough money to withdraw that amount.")
                        else:
                            balance -= withdraw_amount
                            print(f"Your new balance is ${balance:.2f}")
                    elif withdraw_amount == 0.0:
                        print("No money withdrawn")
                    else:
                        # negative amounts, NaN
                        print("Not a valid amount of money to withdraw")
                except ValueError:
                    print("Not a valid input")
            case "4":
                # Transfer
                try:
                    transfer_amount = float(
                        input("How much would you like to transfer: $"))
                    if transfer_amount > 0.0 and transfer_amount != float("inf"):
                        if transfer_amount > balance:
                            print(
                                "You don't have enough money to transfer that amount.")
                        else:
                            balance -= transfer_amount
                            print(f"Your new balance is ${balance:.2f}")
                    elif transfer_amount == 0.0:
                        print("No money transfered")
                    else:
                        # negative amounts, NaN
                        print("Not a valid amount of money to transfer")
                except ValueError:
                    print("Not a valid input")
            case "5":
                # Exit
                print("Exiting")
                break
            case _:
                print("Invalid selection")

        print()
except Exception as e:
    print(f"Error: {e}")
