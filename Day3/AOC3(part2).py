# day3_part2.py
def best_12(line: str) -> int:
    digits = [int(c) for c in line.strip()]
    need = 12
    n = len(digits)
    drop = n - need
    stack = []
    for i, d in enumerate(digits):
        while drop and stack and stack[-1] < d and len(stack) - 1 + (n - i) >= need:
            stack.pop()
            drop -= 1
        stack.append(d)
    if drop:
        stack = stack[:-drop]
    res = stack[:need]
    return int("".join(map(str, res)))

def solve(path="inputAOC3.txt"):
    total = 0
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            total += best_12(s)
    print(total)

if __name__ == "__main__":
    solve()