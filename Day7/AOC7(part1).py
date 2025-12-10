# day7_part1.py
from collections import deque

def solve(path="inputAOC7.txt"):
    grid = [list(l.rstrip("\n")) for l in open(path) if l.strip()]
    R, C = len(grid), len(grid[0])
    sr = sc = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                sr, sc = r, c
    splits = 0
    beams = {(sr + 1, sc)}
    while beams:
        new = set()
        for r, c in beams:
            if not (0 <= r < R and 0 <= c < C):
                continue
            if grid[r][c] == "^":
                splits += 1
                if 0 <= c - 1 < C:
                    new.add((r + 1, c - 1))
                if 0 <= c + 1 < C:
                    new.add((r + 1, c + 1))
            else:
                new.add((r + 1, c))
        beams = new
    print(splits)

if __name__ == "__main__":
    solve()
