# day11_part2.py
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
    def count_paths(node: str, have_dac: bool, have_fft: bool) -> int:
        # Update flags based on current node
        have_dac_now = have_dac or (node == "dac")
        have_fft_now = have_fft or (node == "fft")

        if node == "out":
            # Only count paths that have visited both dac and fft
            return 1 if (have_dac_now and have_fft_now) else 0

        if node not in G:
            return 0

        return sum(
            count_paths(nxt, have_dac_now, have_fft_now)
            for nxt in G[node]
        )

    print(count_paths("svr", False, False))

if __name__ == "__main__":
    solve()