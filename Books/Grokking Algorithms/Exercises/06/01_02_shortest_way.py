from collections import deque, defaultdict

GRAPH_1 = {
    "START": ["T1", "B1"],
    "T1": ["M1", "END"],
    "B1": ["M1", "B2"],
    "M1": [],
    "B2": ["END"],
    "END": []
}
GRAPH_1_RES = ["START", "T1", "END"]


GRAPH_2 = {
    "START": ["M1", "B1"],
    "M1": ["T1", "END"],
    "B1": ["M1", "B2"],
    "T1": ["END"],
    "B2": ["END"],
    "END": []
}
GRAPH_2_RES = ["START", "M1", "END"]


GRAPH_3 = {
    "START": ["M1", "B1"],
    "M1": ["T1"],
    "B1": ["M1", "B2"],
    "T1": ["END"],
    "B2": ["END"],
    "END": []
}
GRAPH_3_RES = ["START", "M1", "T1", "END"]


INF = float("inf")


def shortest_way_exists(
        graph: dict[str, list[str]],
        start: str = "START",
        end: str = "END"
) -> bool:
    """ Алгоритм проверки наличия кратчайшего пути """
    visited = set()
    visit_queue = deque([start])

    while visit_queue:
        node = visit_queue.popleft()
        if node in visited:
            continue

        visited.add(node)
        visit_queue.extend(graph[node])
        for neighbor in graph[node]:
            if neighbor == end:
                return True

    return False


def shortest_way(
        graph: dict[str, list[str]],
        start: str = "START",
        end: str = "END"
) -> list[str] | None:
    """ Алгоритм поиска кратчайшего пути """
    costs = defaultdict(lambda: INF)
    costs[start] = 0
    parents: dict[str, str | None] = defaultdict(lambda: None)

    visited = set()
    visit_queue = deque([start])

    # Поиск кратчайшего пути
    while visit_queue:
        node = visit_queue.popleft()
        if node in visited:
            continue

        visited.add(node)
        visit_queue.extend(graph[node])
        for neighbor in graph[node]:
            new_cost = costs[node] + 1
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node

            # Прерываем, если достигли конца
            if neighbor == end:
                break
        else:
            continue
        break

    # Маршрута нет
    if not parents[end]:
        return None

    # Маршрут есть. Восстанавливаем путь
    path = [end]
    next_node = parents[end]
    while next_node:
        path.append(next_node)
        next_node = parents[next_node]

    return path[::-1]


if __name__ == "__main__":
    for graph_name, graph_, valid_res in (
            ("1", GRAPH_1, GRAPH_1_RES),
            ("2", GRAPH_2, GRAPH_2_RES),
            ("3", GRAPH_3, GRAPH_3_RES)
    ):
        calc_res = shortest_way(graph_)
        print(
            f"Graph {graph_name}",
            f"Valid res: {valid_res}",
            f"Calc. res: {calc_res}",
            "-" * 50,
            sep="\n"
        )
        assert shortest_way_exists(graph_) is True
        assert calc_res == valid_res

    wayless_graph = {"START": ["T1"], "T1": [], "END": []}
    assert shortest_way_exists(wayless_graph) is False
    assert shortest_way(wayless_graph) is None
