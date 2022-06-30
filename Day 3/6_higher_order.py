
# Higher Order do one or both of the following:
# 1. Accepts one or more functions as an argument
# 2. Returns a function

def shout(words):
    return words.upper()


def whisper(words):
    return words.lower()


def normal(words):
    return words.capitalize()


def talk(function_input):
    # storing the function in a variable
    greeting = function_input("This text is created by a function passed as an argument.")
    print(greeting)


talk(shout)
talk(whisper)
talk(normal)

my_list = ["dog", "cat", "mouse", "dragon"]

# Map is a built in higher order function
mapped_list = list(map(str.upper, my_list))
print(mapped_list)

# Filter is a build in function
filtered = list(filter(lambda x: len(x) == 3, my_list))
print(filtered)

