def quick_sort(list: list, key: callable = None, reversed: bool = False) -> list:
    # If the list has only one element, return it as it is already sorted
    if len(list) <= 1:
        return list

    left = 0
    right = len(list) - 1

    sort(list, left, right, key, reversed)
    return list


def sort(
    list: list, left: int, right: int, key: callable = None, reversed: bool = False
) -> list:
    # If the left index is greater than or equal to the right index, the list is already sorted
    # The sub-list has only one or zero elements
    if left >= right:
        return 

    pivot_index = partition(list, left, right, key, reversed)
    sort(list, left, pivot_index - 1, key, reversed)
    sort(list, pivot_index + 1, right, key, reversed)


def partition(
    list: list, left: int, right: int, key: callable = None, reversed: bool = False
) -> int:
    # Choose the last element as the pivot
    if key is not None:
        pivot = key(list[right])
    else:
        pivot = list[right]

    # Index of the greater element
    i = left - 1

    # Iterate through the list
    for j in range(left, right):
        if key is not None:
            current = key(list[j])
        else:
            current = list[j]

        # If the current element is greater than the pivot, swap it with the element at index i
        if (
            (current < pivot and not reversed)
            or (current > pivot and reversed)
            or (current == pivot)
        ):
            i += 1
            list[i], list[j] = list[j], list[i]

    # Swap the pivot with the element at index i + 1
    list[i + 1], list[right] = list[right], list[i + 1]

    # Return the index of the pivot
    return i + 1
