from random import shuffle
from string import ascii_letters


def quick_sort(items: list[int | float | str]) -> list[int | float | str]:
    """
    Быстрая сортировка
    Временная сложность (Средний и лучший): O(N * log N), где N длинна массива
    Временная сложность (Худший): O(N ^ 2), где N длинна массива
    Пространственная сложность: O(N * log N)
    """
    if len(items) < 2:
        return items

    middle = len(items) // 2
    middle_val = items[middle]

    return quick_sort(
        [v for i, v in enumerate(items) if i != middle and v < middle_val]
    ) + [middle_val] + quick_sort(
        [v for i, v in enumerate(items) if i != middle and v > middle_val]
    )


if __name__ == "__main__":
    sorted_digits = list(range(10))
    unsorted_digits = sorted_digits.copy()
    shuffle(unsorted_digits)
    assert sorted_digits == quick_sort(unsorted_digits.copy())

    sorted_letters = sorted(ascii_letters)
    unsorted_letters = sorted_letters.copy()
    shuffle(unsorted_letters)
    assert sorted_letters == quick_sort(unsorted_letters.copy())
