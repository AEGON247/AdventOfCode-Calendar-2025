# day7_part2.py
from functools import lru_cache

def solve(path="inputAOC7.txt"):
    grid = [list(l.rstrip("\n")) for l in open(path) if l.strip()]
    R, C = len(grid), len(grid[0])
    sr = sc = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                sr, sc = r, c

    @lru_cache(maxsize=None)
    def dfs(r, c):
        if not (0 <= r < R and 0 <= c < C):
            return 1
        if grid[r][c] == "^":
            return dfs(r + 1, c - 1) + dfs(r + 1, c + 1)
        else:
            return dfs(r + 1, c)

    print(dfs(sr + 1, sc))

if __name__ == "__main__":
    solve()
