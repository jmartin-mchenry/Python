import math

"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Global Constants BASES and FRUITS defined as Tuples.
[X] 3. Professional function get_price(size) returns a float.
[X] 4. Professional function blend(size, base, fruit, scoops) for output.
[X] 5. main() function handles try/except for scoops (int).
[X] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
SIZES = ("Small", "Medium", "Large")
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# TODO: Define get_price(size)


def get_price(size):
    match size:
        case "Small":
            return 3.0
        case "Medium":
            return 4.0
        case "Large":
            return 5.0
        case _:
            print("invalid size")
            return -1.0

# TODO: Define blend(size, base, fruit, scoops)


def blend(size, base, fruit, scoops):
    print("Blend order: ")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")


def choice(enum, name, prompt):
    # enum is the tuple to use for values
    # name should be a human readable name to be printed
    # prompt should be the user prompt to be displayed
    # errors if the internal input() or int() return an error, or if the index is not in bounds

    print(f"{name}:")
    for i in range(0, len(enum)):
        value = enum[i]
        print(f"[{i + 1}]: {value}")

    index = int(input(f"{prompt} [1..{len(enum)}]: ")) - 1
    value = enum[index]
    return value

# TODO: Define main() to collect input and call your logic


def main():
    try:
        size = choice(SIZES, "Sizes", "What size do you want?")

        price = get_price(size)
    except Exception:
        print("Not a valid size")
        return

    if price < 0.0:
        return
    print()

    try:
        base = choice(BASES, "Bases", "What base do you want?")
    except Exception:
        print("Not a valid base")
        return
    print()

    try:
        fruit = choice(FRUITS, "Fruits", "What fruit do you want?")
    except Exception:
        print("Not a valid fruit")
        return
    print()

    try:
        scoops = int(input("How many scoops would you like? (1 or more): "))
    except Exception:
        print("Not a valid amount of scoops")
        return

    if scoops < 1 or not math.isfinite(scoops):
        print("Not a valid amount of scoops")
        return

    blend(size, base, fruit, scoops)


main()
