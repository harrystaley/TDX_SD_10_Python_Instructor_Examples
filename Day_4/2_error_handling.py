# interpreter raised exception
print(100 / 0)

# developer raised exception
number = int(input("Please input a number between 0 and 10:"))

if 0 < number < 10:
    print(number)
else:
    raise ValueError("The number should be between 0 and 10")

# lets revise with try except
try:
    number = int(input("Please input a number between 0 and 10 to be cubed:"))
    if 0 < number < 10:
        print(number)
    else:
        raise ValueError("The number should be between 0 and 10")
except ValueError as e:
    print(f"ERROR: {e}")
    pass
else:
    print(number ** 3)
