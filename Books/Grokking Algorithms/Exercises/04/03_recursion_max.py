"""
Задача: Найти максимальное число в списке
"""
from typing import Sequence
from random import shuffle


def max_simple(items_: Sequence[int | float]) -> int | float | None:
    if not items_:
        msg = "items is empty"
        raise ValueError(msg)

    m = items_[0]
    for el in items_[1:]:
        if el > m:
            m = el

    return m


def max_recursion_v1(items_: Sequence[int | float]) -> int | float | None:
    """ Первичное решение """
    if len(items_) == 0:
        return None
    elif len(items_) == 1:
        return items_[0]

    if items_[0] < (res := max_recursion_v1(items_[1:])):
        return res
    return items_[0]


def max_recursion_v2(items_: Sequence[int | float]) -> int | float | None:
    """
    Книжное решение

    Годится только при len >= 2. При 1 впадает в бесконечную рекурсию
    """
    if len(items_) == 2:
        return items_[0] if items_[0] > items_[1] else items_[1]

    sub_max = max_recursion_v2(items_[1:])
    return items_[0] if items_[0] > sub_max else sub_max


if __name__ == "__main__":
    max_func = max_recursion_v1
    for i in range(10):
        items = list(range(i + 1))
        shuffle(items)
        max_val = max_func(items)
        assert max(items) == max_val, f"{max(items)=} != {max_val=}"
        print(f"{max_val:>3} is max in {items}")
