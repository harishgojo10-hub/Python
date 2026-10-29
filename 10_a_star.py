import heapq

graph = {
    "A": [("B", 1), ("C", 2)], "B": [("D", 4), ("E", 2)],
    "C": [("F", 2)], "D": [("G", 3)], "E": [("G", 1)],
    "F": [("G", 2)], "G": []
}
heuristic = {"A": 5, "B": 4, "C": 3, "D": 3, "E": 1, "F": 2, "G": 0}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}
    while queue:
        f, cost, node, path = heapq.heappop(queue)
        if node == goal:
            return path, cost
        if cost > best_cost.get(node, float("inf")):
            continue
        for neighbor, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                heapq.heappush(queue, (new_cost + heuristic[neighbor],
                                       new_cost, neighbor, path + [neighbor]))
    return None, None

path, cost = astar("A", "G")
print("A* Path:", " -> ".join(path) if path else "No path found")
print("Total cost:", cost)
