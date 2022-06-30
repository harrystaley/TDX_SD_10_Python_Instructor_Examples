
new = [1, 2, 3]


# this is a impure function
def get_cubes(original):
    for i in original:
        new.append(i**3) # External values modified
    return new  # returns an output NOT SOLELY dependent upon the input


list1 = [1, 2, 3, 4]
list1_cubes = get_cubes(list1)

print("Original List:", list1)
print("Modified List:", list1_cubes)

