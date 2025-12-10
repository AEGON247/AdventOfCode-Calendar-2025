# day6_part2.py
def parse(path="inputAOC6.txt"):
    lines = [l.rstrip("\n") for l in open(path)]
    w = max(len(l) for l in lines)
    lines = [l.ljust(w) for l in lines]
    is_space_col = [all(row[c] == " " for row in lines) for c in range(w)]
    segs = []
    start = None
    for c in range(w):
        if not is_space_col[c]:
            if start is None:
                start = c
        else:
            if start is not None:
                segs.append((start, c - 1))
                start = None
    if start is not None:
        segs.append((start, w - 1))
    return lines, segs

def solve(path="inputAOC6.txt"):
    lines, segs = parse(path)
    problems = []
    for a, b in segs:
        block = [row[a:b+1] for row in lines]
        op_row = max(i for i, r in enumerate(block) if any(ch.strip() for ch in r))
        op_line = block[op_row]
        op = "*" if "*" in op_line else "+"

        cols = list(range(b - a + 1))
        data_cols = [c for c in cols if any(block[r][c] != " " for r in range(op_row))]
        nums = []
        for c in reversed(data_cols):
            digits = [block[r][c] for r in range(op_row) if block[r][c].isdigit()]
            if digits:
                nums.append(int("".join(digits)))
        problems.append((op, nums))

    total = 0
    for op, nums in problems:
        if op == "+":
            total += sum(nums)
        else:
            v = 1
            for x in nums:
                v *= x
            total += v
    print(total)

if __name__ == "__main__":
    solve()
