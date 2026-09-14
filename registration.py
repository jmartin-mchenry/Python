"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""
try:
    while True:
        first_name = input("Enter your first name: ").strip()
        if len(first_name) > 0:
            break
        print("First name should not be empty!")

    while True:
        last_name = input("Enter your last name: ").strip()
        if len(last_name) > 0:
            break
        print("Last name should not be empty!")

    while True:
        try:
            age = int(input("Enter your age: ").strip())
        except ValueError:
            print("Age should be an integer")
            # go back to start of loop so we don't see the 0 or less error
            continue
        if age >= 0:
            break
        print("Age should be greater than or equal to 0")

    while True:
        phone_number = input("Enter your phone number: ").strip()
        if len(phone_number) > 0:
            break
        print("Phone number should not be empty!")

    while True:
        try:
            ticket_count = int(input("Enter your ticket count: ").strip())
        except ValueError:
            print("Tickets should be an integer")
            # go back to start of loop so we don't see the 0 or less error
            continue
        if ticket_count > 0:
            break
        print("Tickets should be greater than 0")

    while True:
        additional_tickets = input("Do you want additional tickets [Y/N]: ").strip().upper()
        if additional_tickets == "Y":
            additional_tickets = True
            break
        elif additional_tickets == "N":
            additional_tickets = False
            break
        else:
            print("Please enter Y or N!")

    if age >= 21:
        print("You get a drink ticket")
except EOFError:
    print()
    print("Unexpected end of file")
except Exception as e:
    print(f"Error: {e}")
