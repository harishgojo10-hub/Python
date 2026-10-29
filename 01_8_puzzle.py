from collections import deque

def solve(start, goal):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        zero = state.index(0)
        row, col = divmod(zero, 3)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = list(state)
                index = nr * 3 + nc
                new_state[zero], new_state[index] = new_state[index], new_state[zero]
                new_state = tuple(new_state)
                if new_state not in visited:
                    queue.append((new_state, path + [state]))
    return None

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
solution = solve(start, goal)
print("8-Puzzle Solution:")
if solution:
    for state in solution:
        print(state[:3]); print(state[3:6]); print(state[6:]); print()
else:
    print("No solution found")
