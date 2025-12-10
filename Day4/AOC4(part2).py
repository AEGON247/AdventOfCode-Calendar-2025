# day4_part2.py
def accessible_positions(grid):
    h, w = len(grid), len(grid[0])
    res = []
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
                res.append((i, j))
    return res

def simulate(grid):
    g = [row[:] for row in grid]
    removed = 0
    while True:
        acc = accessible_positions(g)
        if not acc:
            break
        for i, j in acc:
            g[i][j] = "."
            removed += 1
    return removed

def solve(path="inputAOC4.txt"):
    with open(path) as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    print(simulate(grid))

if __name__ == "__main__":
    solve()