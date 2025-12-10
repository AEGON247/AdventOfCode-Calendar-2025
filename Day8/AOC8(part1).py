# day8_part1.py
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
    sel = pairs[:1000]

    parent = list(range(n))
    size = [1]*n

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    for _, i, j in sel:
        union(i, j)

    comp = {}
    for i in range(n):
        r = find(i)
        comp[r] = comp.get(r, 0) + 1
    sizes = sorted(comp.values(), reverse=True)
    ans = sizes[0] * sizes[1] * sizes[2]
    print(ans)

if __name__ == "__main__":
    solve()
