queue = []


# enqueue
queue.append('a')
queue.append('b')
queue.append('c')

# print our queue
print(f'Queue:{queue}')

# deque all of the items.
for _ in range(len(queue)):
    print(f"deque: {queue.pop(0)}")
    print(f"queue: {queue}")
