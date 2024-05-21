"""
Задача: Вычислить количество через рекурсию
"""
from typing import Sequence


def count_(items_: Sequence) -> int:
    if not items_:
        return 0
    return 1 + count_(items_[1:])


if __name__ == "__main__":
    for i in range(10):
        items = list(range(i + 1))
        items_count = count_(items)
        print(f"{items_count:>3} = count{items}")
        assert len(items) == items_count, f"{len(items)=} != {items_count=}"
