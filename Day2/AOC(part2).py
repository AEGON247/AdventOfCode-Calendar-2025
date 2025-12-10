# day2_part2.py
def is_invalid_repeat(n: int) -> bool:
    s = str(n)
    l = len(s)
    for k in range(1, l // 2 + 1):
        if l % k != 0:
            continue
        m = l // k
        if m < 2:
            continue
        if s[:k] * m == s:
            return True
    return False

def solve(path="inputAOC2.txt"):
    with open(path) as f:
        text = f.read().strip()
    ranges = [r for r in text.split(",") if r]
    total = 0
    for r in ranges:
        a, b = map(int, r.split("-"))
        for x in range(a, b + 1):
            if is_invalid_repeat(x):
                total += x
    print(total)

if __name__ == "__main__":
    solve()