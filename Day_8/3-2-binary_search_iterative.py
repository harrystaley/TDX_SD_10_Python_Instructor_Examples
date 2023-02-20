def binary_search(list_items, target):
    """
    Bnary search executes in logarithmic O(log(n)) time.
    It assumes that items are already sorted in ascending order.
    :param list_items: A list of sorted integers in ascending order.
    :param target: The integer you want found.
    :return: The index of the target otherwise -1
    """
    start = 0  # the index of first item in our list.
    end = len(list_items) - 1  # the index of the last item in our list.

    while start <= end:
        mid = (end + start) // 2
        # If target is greater, ignore left.
        if list_items[mid] < target:
            start = mid + 1
        # If target is smaller, ignore the right half.
        elif list_items[mid] > target:
            end = mid - 1
        else:  # means target is present at mid
            return mid
    # target was not in the list.
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 40
    print(f"The index of {x} in {arr} is {'not in list' if binary_search(arr, x) == -1 else binary_search(arr, x)}.")
