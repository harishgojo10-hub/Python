from itertools import permutations

cities = ["A", "B", "C", "D"]
distance = {
    "A": {"A": 0, "B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "B": 0, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "C": 0, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30, "D": 0}
}
start = "A"
best_path, best_cost = None, float("inf")
for permutation in permutations(city for city in cities if city != start):
    path = [start, *permutation, start]
    cost = sum(distance[path[i]][path[i+1]] for i in range(len(path)-1))
    if cost < best_cost:
        best_path, best_cost = path, cost
print("Best path:", " -> ".join(best_path))
print("Minimum cost:", best_cost)
