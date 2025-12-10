# day8_part2.py
def solve(path="inputAOC8.txt"):
    pts = []
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            x, y, z = map(int, s.split(","))
            pts.append((x, y, z))
    n = len(pts)

    pairs = []
    for i in range(n):
        x1, y1, z1 = pts[i]
        for j in range(i + 1, n):
            x2, y2, z2 = pts[j]
            dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
            d2 = dx*dx + dy*dy + dz*dz
            pairs.append((d2, i, j))
    pairs.sort(key=lambda x: x[0])

    parent = list(range(n))
    size = [1]*n

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    components = n
    last = None
    for d2, i, j in pairs:
        ri, rj = find(i), find(j)
        if ri == rj:
            continue
        if size[ri] < size[rj]:
            ri, rj = rj, ri
        parent[rj] = ri
        size[ri] += size[rj]
        components -= 1
        last = (i, j)
        if components == 1:
            break

    x1 = pts[last[0]][0]
    x2 = pts[last[1]][0]
    print(x1 * x2)

if __name__ == "__main__":
    solve()
