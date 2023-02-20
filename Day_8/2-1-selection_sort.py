def selection_sort(list_items):
    """
    Uses selection sort to return a sorted list in quadratic O(n^2) time.
    :param list_items: A list of integers.
    :return:  list: A list of integers sorted in ascending order..
    """
    lst_len = len(list_items)
    for cur_idx in range(lst_len):
        # Find the minimum element in remaining unsorted list
        min_idx = cur_idx
        for sub_idx in range(cur_idx + 1, lst_len):
            if list_items[min_idx] > list_items[sub_idx]:
                min_idx = sub_idx

        # Swap the min with the current
        list_items[cur_idx], list_items[min_idx] = list_items[min_idx], list_items[cur_idx]
    return list_items


if __name__ == "__main__":
    elements = [39, 12, 18, 85, 72, 10, 2, 18]
    print(f"Unsorted list:\n{elements}")
    print(f"Sorted list:\n{selection_sort(elements)}")
