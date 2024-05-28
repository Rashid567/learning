from collections import deque

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


def shortest_way(
        graph: dict[str, list[str]],
        start_point: str,
        end_point: str
) -> list[str] | None:
    need_to_visit = deque()
    need_to_visit.append(start_point)
    costs = {k: 0 if k == start_point else float("inf") for k in graph}
    visited = set()

    current_point = start_point
    while need_to_visit:
        current_point = need_to_visit.popleft()
        if current_point == end_point:
            break
        if current_point in visited:
            continue

        visited.add(current_point)
        for neighbor in graph[current_point]:
            costs[neighbor] = costs[current_point] + 1
            need_to_visit.extend(graph[neighbor])

    if current_point != "END":
        return None

    res = [current_point]
    max_cost = max((e for e in costs.values() if e != float("inf")))

    while max_cost >= 0:
        current_point = next(
            point for point, neighbors in graph.items()
            if costs[point] == max_cost and current_point in neighbors
        )
        max_cost -= 1
        res.append(current_point)

    return res[::-1]


if __name__ == "__main__":
    for graph_, correct_res in (
            (GRAPH_1, GRAPH_1_RES),
            (GRAPH_2, GRAPH_2_RES),
            (GRAPH_3, GRAPH_3_RES)
    ):
        calc_res = shortest_way(graph_, "START", "END")
        print(calc_res)
        assert calc_res == correct_res
