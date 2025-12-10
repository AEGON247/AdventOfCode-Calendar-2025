# day2_part1.py
def is_invalid_once(n: int) -> bool:
    s = str(n)
    l = len(s)
    if l % 2 == 1:
        return False
    h = l // 2
    return s[:h] == s[h:]

def solve(path="inputAOC2.txt"):
    with open(path) as f:
        text = f.read().strip()
    ranges = [r for r in text.split(",") if r]
    total = 0
    for r in ranges:
        a, b = map(int, r.split("-"))
        for x in range(a, b + 1):
            if is_invalid_once(x):
                total += x
    print(total)

if __name__ == "__main__":
    solve()