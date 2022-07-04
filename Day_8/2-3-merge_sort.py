def merge_sort(list_items):
    """
    Uses merge sort to return a sorted list in quadratic loglinear O(n log(n)) time.
    :param list_items: A list of integers.
    :return:  list: A list of integers sorted in ascending order..
    """
    if len(list_items) > 1:
        mid = len(list_items) // 2
        left = list_items[:mid]
        right = list_items[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        left_idx = 0
        right_idx = 0

        # Iterator for the main list
        main_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                # The value from the left half has been used
                list_items[main_idx] = left[left_idx]
                # Move the iterator forward
                left_idx += 1
            else:
                list_items[main_idx] = right[right_idx]
                right_idx += 1
            # Move to the next slot
            main_idx += 1

        # For all the remaining values
        while left_idx < len(left):
            list_items[main_idx] = left[left_idx]
            left_idx += 1
            main_idx += 1

        while right_idx < len(right):
            list_items[main_idx] = right[right_idx]
            right_idx += 1
            main_idx += 1
    return list_items


if __name__ == "__main__":
    elements = [39, 12, 18, 85, 72, 10, 2, 18]
    print(f"Unsorted list:\n{elements}")
    print(f"Sorted list:\n{merge_sort(elements)}")
