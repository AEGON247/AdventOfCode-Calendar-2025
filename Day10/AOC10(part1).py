# day10_part1.py
import re
from itertools import product

def parse_line(line):
    m = re.match(r"\[(.*?)\](.*)", line)
    pat = m.group(1)
    rest = m.group(2)
    target = [1 if c == "#" else 0 for c in pat]
    n = len(target)
    buttons = []
    for btn in re.findall(r"\(([^)]*)\)", rest.split("{")[0]):
        btn = btn.strip()
        if not btn:
            continue
        idxs = [int(x) for x in btn.split(",")]
        buttons.append(idxs)
    return n, target, buttons

def min_presses_lights(n, target, buttons):
    m_btn = len(buttons)
    A = [[0]*m_btn for _ in range(n)]
    for j, idxs in enumerate(buttons):
        for i in idxs:
            if 0 <= i < n:
                A[i][j] ^= 1
    b = target[:]
    row = 0
    col = 0
    where = [-1]*m_btn
    while row < n and col < m_btn:
        sel = None
        for i in range(row, n):
            if A[i][col]:
                sel = i
                break
        if sel is None:
            col += 1
            continue
        A[row], A[sel] = A[sel], A[row]
        b[row], b[sel] = b[sel], b[row]
        where[col] = row
        for i in range(n):
            if i != row and A[i][col]:
                for j in range(col, m_btn):
                    A[i][j] ^= A[row][j]
                b[i] ^= b[row]
        row += 1
        col += 1
    for i in range(row, n):
        if b[i]:
            return 0
    pivots = [c for c in range(m_btn) if where[c] != -1]
    free_vars = [c for c in range(m_btn) if where[c] == -1]
    best = None
    for assign in product([0, 1], repeat=len(free_vars)):
        x = [0]*m_btn
        for fv, val in zip(free_vars, assign):
            x[fv] = val
        for c in reversed(pivots):
            r = where[c]
            s = b[r]
            for j in range(c+1, m_btn):
                if A[r][j] and x[j]:
                    s ^= 1
            x[c] = s
        w = sum(x)
        if best is None or w < best:
            best = w
    return best if best is not None else 0

def solve(path="inputAOC10.txt"):
    total = 0
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            n, target, buttons = parse_line(s)
            total += min_presses_lights(n, target, buttons)
    print(total)

if __name__ == "__main__":
    solve()