stack = []


# push
stack.append('a')
stack.append('b')
stack.append('c')

# print our stack
print(f'Stack:{stack}')

# peek
print(f"peek: {stack[0]}")

# pop all of the items.
for _ in range(len(stack)):
    popped_item = stack.pop(0)
    print(f"pop: {popped_item}")
    print(f"stack: {stack}")

print('\nstack after elements are popped:')
print(stack)
