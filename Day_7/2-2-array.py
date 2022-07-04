import array as arr

# creating an array with integer type
ints = arr.array('i', [1, 2, 3])

# printing original array
for i in range(0, 3):
    print(ints[i], end=" ")

# creating an array with float type
floats = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(floats[i], end=" ")
