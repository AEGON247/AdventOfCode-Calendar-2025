# day4_part1.py
def count_accessible(grid):
    h, w = len(grid), len(grid[0])
    total = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] != "@":
                continue
            neighbors = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == "@":
                        neighbors += 1
            if neighbors < 4:
                total += 1
    return total

def solve(path="inputAOC4.txt"):
    with open(path) as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    print(count_accessible(grid))

if __name__ == "__main__":
    solve()