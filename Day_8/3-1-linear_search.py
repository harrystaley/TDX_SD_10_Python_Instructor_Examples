def linear_search(list_items, target):
    """
    Use a lindear search to find an integer in a list in linear O(n) time.
    :param list_items: A list of integers.
    :param target: An integer
    :return: The index of the integer if found otherwise -1
    """
    lst_len = len(list_items)
    for target_idx in range(lst_len):
        if list_items[target_idx] == target:
            return target_idx
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    print(f"The index of {x} in {arr} is {'not in list' if linear_search(arr, x) == -1 else linear_search(arr, x) }.")
