def merge_sort(list: list, key: callable = None, reversed: bool = False) -> list:
    # If the list has only one element, return it as it is already sorted
    if len(list) <= 1:
        return list

    left = 0
    right = len(list) - 1
    divide(list, left, right, key, reversed)
    return list


def divide(
    list: list, left: int, right: int, key: callable = None, reversed: bool = False
) -> list:
    if left < right:
        middle = (left + right) // 2

        divide(list, left, middle, key, reversed)
        divide(list, middle + 1, right, key, reversed)
        merge(list, left, middle, right, key, reversed)


def merge(
    list: list,
    left: int,
    middle: int,
    right: int,
    key: callable = None,
    reversed: bool = False,
) -> list:
    left_list = list[left : middle + 1]
    right_list = list[middle + 1 : right + 1]

    left_index = 0
    right_index = 0
    merged_index = left
    # print(f"Merging {left_list} and {right_list}")

    while left_index < len(left_list) and right_index < len(right_list):
        left_value = left_list[left_index]
        right_value = right_list[right_index]

        if key is not None:
            left_value = key(left_value)
            right_value = key(right_value)
            # print(f"{left_index = }, {right_index = }, {merged_index = }")
            # print(f"Comparing {left_value} and {right_value}")

        if (
            (left_value < right_value and not reversed)
            or (left_value > right_value and reversed)
            or (left_value == right_value)
        ):
            list[merged_index] = left_list[left_index]
            left_index += 1
        else:
            list[merged_index] = right_list[right_index]
            right_index += 1

        # print(f"Current list: {list}")
        merged_index += 1

    while left_index < len(left_list):
        list[merged_index] = left_list[left_index]
        left_index += 1
        merged_index += 1
        # print(f"Current list: {list}")

    while right_index < len(right_list):
        list[merged_index] = right_list[right_index]
        right_index += 1
        merged_index += 1
        # print(f"Current list: {list}")

    # print("\n")
