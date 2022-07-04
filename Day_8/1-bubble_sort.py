def bubble_sort(list_items):
    """
    Uses bubble sort to return a sorted list in quadratic O(n^2) time.
    :param list_items: A list of integers.
    :return:  list: A list of integers sorted in ascending order..
    """
    # Looping over the list from end to start.
    lst_end = len(list_items) - 1
    lst_start = 0
    for local_end in range(lst_end, lst_start, -1):
        for i in range(local_end):
            # swap values if the element is less than next element.
            if list_items[i] > list_items[i + 1]:
                # swap values.
                list_items[i], list_items[i + 1] = list_items[i + 1], elements[i]
    # return the sorted list.
    return list_items


if __name__ == "__main__":
    elements = [39, 12, 18, 85, 72, 10, 2, 18]
    print(f"Unsorted list:\n{elements}")
    print(f"Sorted list:\n{bubble_sort(elements)}")
