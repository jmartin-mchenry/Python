"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[x] 1. Create a list of 20 seats (numbered 1-20).
[x] 2. Display the list of available seats.
[x] 3. Ask user for a seat number (0 to quit).
[x] 4. Remove the selected seat from the list.
[x] 5. Handle invalid inputs (seat taken or doesn't exist).
[x] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

seats = list(range(1, 21))

while len(seats) > 0:
    print(f"Available seats: {seats}")

    try:
        seat = int(input("Enter a seat to fill (0 to exit): "))
    except ValueError:
        print("Please enter your input as an integer number.")
        continue  # go back to start of loop
    except Exception as e:
        print(f"Error: {e}")
        break

    if seat == 0:
        print("Exiting")
        break

    try:
        seats.remove(seat)
    except ValueError:
        print("That seat doesn't exist or is already taken.")

if len(seats) == 0:
    print("All seats taken, exiting")
