import random

number = 5
# lambda
cube = lambda x: x ** 3
print(cube(number))

# lambda if
number_truth = lambda x: True if (10 < x < 20) else False
print(number_truth(number))

# using lambdas with functions
numbers = [x for x in range(100)]
listofNum = list(filter(lambda x: 10 < x < 20, numbers))
print(listofNum)

animals = ['dog', 'cat', 'bird', 'bird', 'dog']

# list comprehension
generated_nums = [x for x in range(10)]
print(generated_nums)
upper_animals = [animal.upper() for animal in animals]
print(upper_animals)

# set comprehension
animal_set = {animal.upper() for animal in animals}
print(animal_set)

# dict comprehension
animal_values = {animal: random.randint(1, 1000) for animal in animals}
print(animal_values)
