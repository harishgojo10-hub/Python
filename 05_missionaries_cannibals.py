from collections import deque

# State: (missionaries on left, cannibals on left, boat side)
# 0 = left bank, 1 = right bank
def valid(m, c):
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    mr, cr = 3 - m, 3 - c
    if m > 0 and c > m:
        return False
    if mr > 0 and cr > mr:
        return False
    return True

def solve():
    start, goal = (3, 3, 0), (0, 0, 1)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        m, c, boat = state
        for dm, dc in moves:
            nxt = (m-dm, c-dc, 1) if boat == 0 else (m+dm, c+dc, 0)
            if valid(nxt[0], nxt[1]) and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None

solution = solve()
print("Missionaries and Cannibals (M-left, C-left, boat side):")
if solution:
    for state in solution:
        print(state)
    print("Goal reached safely.")
else:
    print("No solution found")
