"""
Задача: Вычислить сумму через рекурсию
"""


def sum_(items_: list[int | float]) -> int | float:
    if not items_:
        return 0
    return items_[0] + sum_(items_[1:])


if __name__ == "__main__":
    total = 0
    for i in range(10):
        total += i
        items = list(range(i + 1))
        items_sum = sum_(items)
        print(f"{items_sum:>3} = sum{items}")
        assert total == items_sum, f"{total=} != {items_sum=}"
