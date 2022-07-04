def insertion_sort(list_items):
    """
    Uses selection sort to return a sorted list in quadratic O(n^2) time.
    :param list_items: A list of integers.
    :return:  list: A list of integers sorted in ascending order..
    """
    lst_len = len(list_items)
    # the left most item is assumed to initially be sorted.
    for key_idx in range(1, lst_len):
        # set key equal to the item at index i
        key = list_items[key_idx]

        swp_idx = key_idx - 1
        # swap items until item at swp_idx is less than key
        while swp_idx >= 0 and key < list_items[swp_idx]:
            list_items[swp_idx + 1] = list_items[swp_idx]
            swp_idx -= 1
        list_items[swp_idx + 1] = key
    return list_items


if __name__ == "__main__":
    elements = [39, 12, 18, 85, 72, 10, 2, 18]
    print(f"Unsorted list:\n{elements}")
    print(f"Sorted list:\n{insertion_sort(elements)}")
