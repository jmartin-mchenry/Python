"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[X] 3. Function 'make_pizza' defines 4 specific parameters.
[X] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[X] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

TOPPINGS = ("Pepperoni", "Sausage", "Bacon", "Pineapple")


def make_pizza(customer, size, topping, is_delivery=False):
    print("Pizza summary: ")
    print(f"{customer} ordered a {size.lower()} pizza with {topping.lower()}.")
    if is_delivery:
        print("This pizza will be delivered.")
    else:
        print("This pizza will not be delivered, and should be picked up at the store.")


def main():
    print("pizza maker thing")

    customer = input("What is your name: ")
    size = input("What size pizza would you like? [small, medium, large]: ")

    print("Available toppings:")
    for i in range(0, len(TOPPINGS)):
        topping = TOPPINGS[i]
        print(f"[{i+1}] {topping}")
    try:
        topping = int(input(f"Choose a topping [1..{len(TOPPINGS)}]: "))
        topping = TOPPINGS[topping - 1]
    except ValueError:
        print("Input should be an integer!")
        return
    except IndexError:
        print("Input should be a valid option!")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    choice = input("Is this a delivery order? [y/n]: ")
    if choice.strip().lower() == "y":
        is_delivery = True
    else:
        is_delivery = False

    make_pizza(customer=customer, size=size,
               topping=topping, is_delivery=is_delivery)


main()
