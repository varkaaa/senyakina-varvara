
from collections import deque

def bfs_shortest_path(graph, entry, exit_point):
    bfs_queue = deque([entry])
    predecessor = {entry: None}
    explored = {entry}

    while bfs_queue:
        current_node = bfs_queue.popleft()
        if current_node == exit_point:
            break

        for adjacent_room in graph.get(current_node, []):
            if adjacent_room not in explored:
                explored.add(adjacent_room)
                predecessor[adjacent_room] = current_node
                bfs_queue.append(adjacent_room)

    if exit_point not in predecessor:
        return None

    shortest_route = []
    current_room = exit_point
    while current_room is not None:
        shortest_route.append(current_room)
        current_room = predecessor[current_room]
    
    shortest_route.reverse()
    return shortest_route

# Граф лабиринта
graph = {
    "S": ["B", "D"],
    "B": ["S", "D", "C"],
    "C": ["B", "J"],
    "J": ["C", "G", "I"],
    "I": ["J"],
    "D": ["S", "B", "E", "G"],
    "E": ["D", "F"],
    "F": ["E", "A", "H"],
    "A": ["F"],
    "H": ["F", "G"],
    "G": ["D", "H", "J"],
}

entry_point = "S"
exit_point = "I"
shortest_path = bfs_shortest_path(graph, entry_point, exit_point)

if shortest_path is None:
    print("Путь не найден")
else:
    print(" -> ".join(shortest_path))
    print("Длина пути (число переходов):", len(shortest_path) - 1)
