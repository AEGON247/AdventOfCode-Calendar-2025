# day11_part1.py
from functools import lru_cache

def build_graph(path="inputAOC11.txt"):
    G = {}
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            name, rest = s.split(":")
            outs = rest.strip().split()
            G[name.strip()] = outs
    return G

def solve(path="inputAOC11.txt"):
    G = build_graph(path)

    @lru_cache(maxsize=None)
    def paths(node: str) -> int:
        if node == "out":
            return 1
        if node not in G:
            return 0
        return sum(paths(nxt) for nxt in G[node])

    print(paths("you"))

if __name__ == "__main__":
    solve()