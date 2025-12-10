# day5_part1.py
def solve(path="inputAOC5.txt"):
    ranges = []
    avail = []
    with open(path) as f:
        section = 0
        for line in f:
            s = line.strip()
            if not s:
                section = 1
                continue
            if section == 0:
                a, b = map(int, s.split("-"))
                ranges.append((a, b))
            else:
                avail.append(int(s))

    ranges.sort()
    merged = []
    for a, b in ranges:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)

    def is_fresh(x):
        for a, b in merged:
            if x < a:
                return False
            if a <= x <= b:
                return True
        return False

    cnt = sum(1 for x in avail if is_fresh(x))
    print(cnt)

if __name__ == "__main__":
    solve()