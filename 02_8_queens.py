def solve_queens(n=8):
    board = [-1] * n
    def safe(row, col):
        for previous_row in range(row):
            previous_col = board[previous_row]
            if previous_col == col or abs(previous_col - col) == abs(previous_row - row):
                return False
        return True
    def backtrack(row):
        if row == n:
            return True
        for col in range(n):
            if safe(row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
                board[row] = -1
        return False
    return board if backtrack(0) else None

solution = solve_queens()
print("8-Queen Solution:")
if solution:
    for col in solution:
        print(" ".join("Q" if j == col else "." for j in range(8)))
else:
    print("No solution found")
