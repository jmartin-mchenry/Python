"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Department constant defined in ALL_CAPS.
[X] 3. Username tuple and password list defined.
[X] 4. While loop runs interactively.
[X] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

DEPARTMENT = ("Legal",)
USERNAMES = ("admin", "john", "jane", "alex", "bob")
# Note: in a secure enviroment, you'd want to salt and hash the passwords to prevent anybody from gaining access to them.
# however, just using a list is the easiest way to fufill the assignment and doesn't require a bunch of extra work.
passwords = ["admin", "password", "12345678",
             "password1234", "pass word 1 2 3 4"]

while True:
    print(f"--- {DEPARTMENT[0].upper()} DEPARTMENT SECURITY TERMINAL ---")
    print("[1] List users")
    print("[2] Update password")
    print("[3] Update username")
    print("[4] Exit")

    choice = input("Enter your input [1..3]: ").strip()
    print()

    match choice:
        case "1":
            for i in range(0, len(USERNAMES)):
                print(f"id: {i}, username: {USERNAMES[i]}, password: {passwords[i]}")

        case "2":
            name = input("Whose password would you like to update: ")
            try:
                index = USERNAMES.index(name)
            except ValueError:
                print("That user does not exist.\n")
                continue
            new_password = input("Enter the new password: ")
            passwords[index] = new_password
            print("Password updated!")

        case "3":
            name = input("Old username: ")
            try:
                index = USERNAMES.index(name)
            except ValueError:
                print("That user does not exist.\n")
                continue
            new_username = input("New username: ")

            try:
                USERNAMES[index] = new_username
                # This code *should* be unreachable, since the above statment should have errored.
                print("Username updated!")
            except TypeError:
                print(
                    "Usernames cannot be updated from this terminal. Please email the help desk to change your username.")

        case "4":
            print("Exiting.")
            break

        case _:
            print("Not a valid option.")

    print()
