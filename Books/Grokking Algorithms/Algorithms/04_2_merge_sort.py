from random import shuffle
from string import ascii_letters


T = list[int | float | str]


def merge(items_1: T, items_2: T) -> T:
    i = j = 0
    max_i = len(items_1)
    max_j = len(items_2)
    res = []

    while i < max_i and j < max_j:
        if items_1[i] < items_2[j]:
            res.append(items_1[i])
            i += 1
        else:
            res.append(items_2[j])
            j += 1

    res.extend(items_1[i:])
    res.extend(items_2[j:])

    print(res)
    return res


def merge_sort(items: list[int | float | str]) -> list[int | float | str]:
    """
    Сортировка слиянием
    Временная сложность: O(N * log N), где N длинна массива
    Пространственная сложность: O(N)
    """
    if len(items) < 2:
        return items

    middle = len(items) // 2

    return merge(
        merge_sort(items[:middle]),
        merge_sort(items[middle:])
    )


if __name__ == "__main__":
    sorted_digits = list(range(10))
    unsorted_digits = sorted_digits.copy()
    shuffle(unsorted_digits)
    assert sorted_digits == merge_sort(unsorted_digits.copy())

    sorted_letters = sorted(ascii_letters)
    unsorted_letters = sorted_letters.copy()
    shuffle(unsorted_letters)
    assert sorted_letters == merge_sort(unsorted_letters.copy())
