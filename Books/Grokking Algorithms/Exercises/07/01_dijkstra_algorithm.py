from collections import defaultdict


GRAPH_A = {
    "START": {
        "T1": 5,
        "B1": 2
    },
    "T1": {
        "T2": 4,
        "B2": 2
    },
    "B1": {
        "T1": 8,
        "B2": 7
    },
    "T2": {
        "END": 3,
        "B2": 6
    },
    "B2": {
        "END": 1
    },
    "END": {}
}

GRAPH_A_RES = (8, ["START", "T1", "B2", "END"])


GRAPH_B = {
    "START": {
        "T1": 10,
    },
    "T1": {
        "T2": 20
    },
    "T2": {
        "END": 30,
        "B1": 1
    },
    "B1": {
        "T1": 1,
    },
    "END": {}
}

GRAPH_B_RES = (60, ["START", "T1", "T2", "END"])


GRAPH_C = {
    "START": {
        "T1": 2,
        "B1": 2
    },
    "T1": {
        "END": 2,
        "B2": 2
    },
    "B1": {
        "T1": 2,
    },
    "B2": {
        "END": 2,
        "B1": -1
    },
    "END": {}
}

GRAPH_C_RES = (4, ["START", "T1", "END"])


INF = float("inf")


def find_lowest(costs: dict[str, float], visited: set[str]) -> str | None:
    """ Поиск не посещённого узла с минимальной стоимостью """
    lowest_cost = INF
    lowest = None

    for node, cost in costs.items():
        if cost < lowest_cost and node not in visited:
            lowest_cost = cost
            lowest = node

    return lowest


def dijkstra(
        graph: dict[str, dict[str, int]],
        start: str = "START",
        end: str = "END"
) -> tuple[float, list[str]]:
    """ Алгоритм Дейкстры """
    costs: dict[str, float] = defaultdict(lambda: INF)
    costs[start] = 0
    parents: dict[str, str | None] = defaultdict(lambda: None)
    visited: set[str] = set()

    # Расчёт стоимости всех переходов
    while node := find_lowest(costs, visited):
        visited.add(node)
        for neighbor, cost in graph[node].items():
            new_cost = costs[node] + cost
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node

    # Маршрута до конечного узла нет
    if not parents[end]:
        return INF, []

    # Маршрут есть. Восстанавливаем путь
    path = [end]
    next_node = parents[end]
    while next_node:
        path.append(next_node)
        next_node = parents[next_node]

    return costs[end], path[::-1]


if __name__ == '__main__':
    for graph_name, graph_, valid_res in (
            ("A", GRAPH_A, GRAPH_A_RES),
            ("B", GRAPH_B, GRAPH_B_RES),
            ("C", GRAPH_C, GRAPH_C_RES),
    ):
        calc_res = dijkstra(graph_)
        print(
            f"Graph {graph_name}",
            f"Valid res: {valid_res}",
            f"Calc. res: {calc_res}",
            "-" * 50,
            sep="\n"
        )
        assert valid_res == calc_res
