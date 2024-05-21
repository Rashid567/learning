from functools import lru_cache


def countdown(n: int) -> None:
    """
    Обратный отсчёт
    Временная сложность: O(N)
    Пространственная сложность: O(1)
    """
    # Базовый случай
    if n < 0:
        print(f"Countdown: Complete")
        return

    # Рекурсивный случай
    print(f"Countdown: {n}...")
    return countdown(n - 1)


@lru_cache
def fibonacci(n: int) -> int:
    """
    Вычисление числа Фибоначчи

    При отсутствии декоратора lru_cache:
        Временная сложность: O(2^N), где 2 - количество ветвлений
        Пространственная сложность: O(N)

    С декоратором lru_cache:
        Временная сложность: O(N), при условии не переполнения кэша
        Пространственная сложность: O(N)
    """
    # Базовый случай
    if n <= 1:
        return n

    # Рекурсивный случай
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    countdown(5)

    print("\nFibonacci:")
    for i, v in enumerate((0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)):
        calc_v = fibonacci(i)
        print(f"  {i:>2} --> {calc_v}")
        assert v == fibonacci(i), f'{v=} != {calc_v=}'
