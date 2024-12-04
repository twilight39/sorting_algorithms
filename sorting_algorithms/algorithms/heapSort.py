def heap_sort(list: list, key: callable = None, reversed: bool = False) -> list:
    heap_size = len(list)

    # For each non-leaf node, heapify the list
    # If node A is a parent node, its left child is at 2 * A + 1 and its right child is at 2 * A + 2
    # The last non-leaf node is at index (heap_size // 2) - 1
    for i in range(heap_size // 2 - 1, -1, -1):
        # print(f"Calling heapify on {i}")
        heapify(list, heap_size, i, key, reversed)

    # Pop the largest/smallest element from the heap and heapify the remaining list
    for i in range(heap_size - 1, 0, -1):
        list[0], list[i] = list[i], list[0]
        # print(f"Popping {list[i]} from the heap\nlist size: {i}")
        # print(f"list: {list}\n")
        heapify(list, i, 0, key, reversed)

    return list


def heapify(
    list: list,
    heap_size: int,
    subtree_root: int,
    key: callable = None,
    reversed: bool = False,
) -> None:
    new_root_index = subtree_root
    left_child = 2 * subtree_root + 1
    right_child = 2 * subtree_root + 2

    if key is not None:
        root_value = key(list[new_root_index])
        if left_child < heap_size and (
            (key(list[left_child]) > root_value and not reversed)
            or (key(list[left_child]) < root_value and reversed)
        ):
            new_root_index = left_child

        if right_child < heap_size and (
            (key(list[right_child]) > key(list[new_root_index]) and not reversed)
            or (key(list[right_child]) < key(list[new_root_index]) and reversed)
        ):
            new_root_index = right_child
    else:
        if left_child < heap_size and (
            (list[left_child] > list[new_root_index] and not reversed)
            or (list[left_child] < list[new_root_index] and reversed)
        ):
            new_root_index = left_child
        if right_child < heap_size and (
            (list[right_child] > list[new_root_index] and not reversed)
            or (list[right_child] < list[new_root_index] and reversed)
        ):
            new_root_index = right_child

    if new_root_index != subtree_root:
        list[subtree_root], list[new_root_index] = (
            list[new_root_index],
            list[subtree_root],
        )
        heapify(list, heap_size, new_root_index, key, reversed)


if __name__ == "__main__":
    heap_sort([2, 4, 8, 6], key=lambda x: -x, reversed=True)
