"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[X] 3. Program takes a word and uppercases it.
[X] 4. Program loops through letters and prints NATO words.
[X] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""
NATO_ALPHABET = {
    "a": "Alfa",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "Xray",
    "y": "Yankee",
    "z": "Zulu",

    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Tree",
    "4": "Fower",
    "5": "Fife",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Niner",
}

# Use a dictionary comprehension to reverse the dictionary
# https://www.geeksforgeeks.org/python/python-dictionary-comprehension/
# `NATO_ALPHABET.items()` returns all key value pairs in NATO_ALPHABET
# We process all of them in the `for letter, word in NATO_ALPHABET.items()`
# We then reverse the letter and the word, and lowercase the word, by defining them as `word.lower(): letter`
# as a side note, I don't really like how understanding a dict comprehension requires reading it backwards, but it works
# I found this solution from https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping#483833,
# and used my previous knowledge of the existence of dict comprehensions to do more research on them and make
# changes required for this dict.
NATO_ALPHABET_REVERSE = {word.lower(): letter for letter,
                         word in NATO_ALPHABET.items()}

while True:
    print("Nato Alphabet Converter")
    print("[1] Convert to Nato alphabet")
    print("[2] Convert from Nato alphabet")
    print("[3] Exit")
    choice = input("[1..3]: ")

    match choice:
        case "1":
            word = input("Enter word to spell: ").lower()

            output = ""

            for letter in word:
                try:
                    output += NATO_ALPHABET.get(letter)
                except:
                    output += letter
                output += " "

            print(output)
        case "2":
            spelling = input("Enter Nato spelling: ").lower()
            words = spelling.split(" ")
            output = ""
            output_valid = True
            for word in words:
                try:
                    letter = NATO_ALPHABET_REVERSE.get(word)
                    output += letter
                except:
                    # If the word contains alphanumeric chars, error, since alphanumeric values outputted from this
                    # program should always be able to be transformed back. If there are no alphanumeric characters, add it
                    # to the output string without erroring
                    is_alpha = False

                    # Note: we intentionally don't just do word.isalnum(), since we need to check for indivual alphanumeric characters
                    for letter in word:
                        if letter.isalnum():
                            is_alpha = True
                    if is_alpha:
                        print(
                            f"Error: input contains a word that can't be converted: {word}")
                        output_valid = False
                        break
                    output += word

            if output_valid:
                print(output)
        case "3":
            print("Exiting")
            break
        case _:
            print("Unknown option")
