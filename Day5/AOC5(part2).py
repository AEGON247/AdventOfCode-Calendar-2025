# day5_part2.py
def solve(path="inputAOC5.txt"):
    ranges = []
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s:
                break
            a, b = map(int, s.split("-"))
            ranges.append((a, b))

    ranges.sort()
    merged = []
    for a, b in ranges:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)

    total = sum(b - a + 1 for a, b in merged)
    print(total)

if __name__ == "__main__":
    solve()
