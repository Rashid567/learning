"""
Бинарный поиск через рекурсию
"""


def binary_search(
        items: list[int | float],
        value: int | float
) -> int | None:
    if not items:
        return None

    lo: int = 0
    hi: int = len(items) - 1
    mid = (hi + lo) // 2
    guess = items[mid]

    if guess == value:
        return mid
    elif guess > value:
        return binary_search(items[:mid], value)

    res = binary_search(items[mid + 1:], value)
    if res is None:
        return None
    return mid + 1 + res


if __name__ == "__main__":
    values = list(range(0, 100, 3))

    for i, val in enumerate(values[3:5], start=3):
        print(f"Searching exists {val=} ...")
        assert (r := binary_search(values, val)) == i, f"{r} != {i}"

    for val in (values[0] - 1, values[-1] + 1):
        print(f"Searching NOT exists {val=} ...")
        assert (r := binary_search(values, val)) is None, f"{r} is not None"
