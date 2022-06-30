
# this is a pure function
def get_cubes(original):
    new = []  # Does not change the input value or any external values.
    for i in original:
        new.append(i**3)  # It always produces the same output given the same input.
    return new  # returns an output SOLELY dependent upon the input


list1 = [1, 2, 3, 4]
list1_cubes = get_cubes(list1)

print("Original List:", list1)
print("Modified List:", list1_cubes)

