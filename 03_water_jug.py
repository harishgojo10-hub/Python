from collections import deque

def solve_water_jug(capacity_a=4, capacity_b=3, target=2):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (a, b), path = queue.popleft()
        if a == target or b == target:
            return path
        pour_a_to_b = min(a, capacity_b - b)
        pour_b_to_a = min(b, capacity_a - a)
        next_states = [
            (capacity_a, b), (a, capacity_b), (0, b), (a, 0),
            (a - pour_a_to_b, b + pour_a_to_b),
            (a + pour_b_to_a, b - pour_b_to_a)
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None

solution = solve_water_jug()
print("Water Jug Solution (4L and 3L jugs; target 2L):")
if solution:
    for state in solution:
        print(state)
else:
    print("No solution found")
