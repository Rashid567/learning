from string import ascii_letters
from random import shuffle


def sort_v1(items: list) -> list:
    """
    Сортировка выбором V1
    Временная сложность: O(N^2), где N длинна массива
    Пространственная сложность: O(N)
    """
    sorted_items = []
    while items:
        min_i = 0
        min_v = items[0]
        for i, v in enumerate(items[1:], start=1):
            if v < min_v:
                min_i, min_v = i, v
        sorted_items.append(items.pop(min_i))

    return sorted_items


def sort_v2(items: list) -> list:
    """
    Сортировка выбором V2
    Временная сложность: O(N^2), где N длинна массива
    Пространственная сложность: O(1)
    """
    for i in range(len(items)):
        min_j = i
        min_v = items[i]
        for j, v in enumerate(items[i + 1:], start=i + 1):
            if v < min_v:
                min_j, min_v = j, v

        items[i], items[min_j] = items[min_j], items[i]

    return items


if __name__ == "__main__":
    sorted_digits = list(range(10))
    unsorted_digits = sorted_digits.copy()
    shuffle(unsorted_digits)
    assert sorted_digits == sort_v1(unsorted_digits.copy())
    assert sorted_digits == sort_v2(unsorted_digits.copy())

    sorted_letters = sorted(ascii_letters)
    unsorted_letters = sorted_letters.copy()
    shuffle(unsorted_letters)
    assert sorted_letters == sort_v1(unsorted_letters.copy())
    assert sorted_letters == sort_v2(unsorted_letters.copy())
