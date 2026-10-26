"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[X] 1. Program uses a while loop to keep asking for bugs.
[X] 2. Uses the datetime module to get a timestamp format.
[X] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[X] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[X] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""
import datetime


def main():
    storage = {}

    while True:
        choice = input("Enter 'log' to record a bug, or 'quit' to stop: ")
        match choice:
            case "log":
                file_name = input("File name: ")
                description = input("Description of error: ")
                priority = input("Priority (High, Medium, Low): ")

                current_time = datetime.datetime.now()
                # small note for fun: using a timestamp does not guarentee uniqueness, since the user
                # can change the system clock while the program is running.
                storage[current_time] = [file_name, description, priority]

            case "quit":
                break
            case _:
                print("Unknown option")

    with open("bug_log.txt", "a") as file:
        for (timestamp, [file_name, description, priority]) in storage.items():
            timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}]\n")
            file.write(f"File: {file_name}\n")
            file.write(f"Status: {description}\n")
            file.write(f"Priority: {priority}\n")
            file.write(
                f"--------------------------------------------------\n")


main()
