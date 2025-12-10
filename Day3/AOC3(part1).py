# day3_part1.py
def max_pair(line: str) -> int:
    digits = [int(c) for c in line.strip()]
    best = -1
    n = len(digits)
    for i in range(n):
        for j in range(i + 1, n):
            v = digits[i] * 10 + digits[j]
            if v > best:
                best = v
    return best

def solve(path="inputAOC3.txt"):
    total = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += max_pair(line)
    print(total)

if __name__ == "__main__":
    solve()
