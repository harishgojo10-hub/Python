graph = {
    "A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
    "D": [], "E": [], "F": []
}

def dfs(node, visited, order):
    if node not in visited:
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited, order)

order = []
dfs("A", set(), order)
print("DFS Traversal:", " ".join(order))
