"""
Бинарный поиск

Временная сложность: O(Log N), где N длинна массива
Пространственная сложность: O(1)
"""

import bisect

from prettytable import PrettyTable


def binary_search_v1(
        search_list: list[int | float],
        value: int | float
) -> int | None:
    hi = len(search_list)
    index = bisect.bisect_left(search_list, value, hi=hi)
    return index if index != hi and search_list[index] == value else None


def binary_search_v2(
        search_list: list[int | float],
        value: int | float,
        print_res: bool = False
) -> int | None:
    res: int | None = None
    step: int = 0
    lo: int = 0
    hi: int = len(search_list) - 1

    table = PrettyTable()
    if print_res:
        table.title = f"Searching: {value}. Array length: {len(search_list)}. "
        table.field_names = [
            "Step", "Left idx", "Middle idx", "Right idx", "Guess"
        ]

    while lo <= hi:
        step += 1
        mid = (hi + lo) // 2
        guess = search_list[mid]
        if step > 10:
            raise Exception
        if print_res:
            table.add_row([step, lo, mid, hi, guess])

        if guess == value:
            res = mid
            break

        if guess > value:
            hi = mid - 1
        else:
            lo = mid + 1

    if print_res:
        table.title += f"Result: {res}"
        print(table)

    return res


if __name__ == "__main__":
    values = list(range(0, 100, 3))

    for i, val in enumerate(values[3:5], start=3):
        assert (r := binary_search_v1(values, val)) == i, f"{r} != {i}"
        assert (r := binary_search_v2(values, val)) == i, f"{r} != {i}"

    for val in (values[0] - 1, values[-1] + 1):
        assert (r := binary_search_v1(values, val)) is None, f"{r} is not None"
        assert (r := binary_search_v2(values, val)) is None, f"{r} is not None"
