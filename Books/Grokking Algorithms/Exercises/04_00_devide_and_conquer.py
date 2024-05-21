"""
Задача: Разделяй и властвуй

Дано поле 1680м х 640м.
Необходимо разделить поле на квадраты равных размеров
"""


def calc(a: int, b: int) -> tuple[int, int]:
    min_, max_ = (a, b) if a < b else (b, a)
    if (remainder := max_ % min_) == 0:
        return min_, min_
    return calc(min_, remainder)


if __name__ == "__main__":
    print("Result:", calc(10, 1))
    print("Result:", calc(25, 5))
    print("Result:", calc(1680, 640))
