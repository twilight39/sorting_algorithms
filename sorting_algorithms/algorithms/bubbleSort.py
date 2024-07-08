def bubble_sort(data: list[list[str]], index: int = 0) -> list[str]:
    n = len(data)
    swapped = True

    while swapped is True:
        swapped = False
        for i in range(1, n):
            if data[i - 1][index] > data[i][index]:
                data[i - 1], data[i] = data[i], data[i - 1]
                swapped = True

    return data
