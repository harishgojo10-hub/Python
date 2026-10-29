from collections import deque

graph = {
    "A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
    "D": [], "E": [], "F": []
}

def bfs(start):
    visited, queue, order = set(), deque([start]), []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    return order

print("BFS Traversal:", " ".join(bfs("A")))
