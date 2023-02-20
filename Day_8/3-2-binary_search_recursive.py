def binary_search(list_items, target, start=None, end=None):
    """
    Binary search executes in logarithmic O(log(n)) time.
    It assumes that items are already sorted in ascending order.
    :param list_items: A list sorted in ascending order.
    :param target: The integer you are searching for.
    :param start: DO NOT MODIFY: Where the recursive call starts.
    :param end: DO NOT MODIFY: Where the recursive call ends.
    :return: The index of the integer you are searching for.
    """
    # set starting params if they were not provided.
    if not start:
        start = 0
    if not end:
        end = len(list_items)

    # Check base case
    if end >= start:
        mid = (end + start) // 2
        # If target is the middle.
        if list_items[mid] == target:
            return mid
        # If target is smaller than mid, check the left sublist
        elif list_items[mid] > target:
            return binary_search(list_items, target, start, mid - 1)
        # Else the target may be in the right sublist.
        else:
            return binary_search(list_items, target, mid + 1, end)
    else:
        # target is not in the list
        return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 40
    print(f"The index of {x} in {arr} is {'not in list' if binary_search(arr, x) == -1 else binary_search(arr, x) }.")
