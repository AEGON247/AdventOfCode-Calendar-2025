import numpy as np

INPUT_FILE = "inputAOC9.txt"

def read_points(path=INPUT_FILE):
    pts = []
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            x, y = map(int, s.split(","))
            pts.append((x, y))
    return pts

def build_compressed_grid(points):
    xs = sorted({x for x, _ in points})
    ys = sorted({y for _, y in points})

    # ranks and gaps
    vx = []
    last = None
    for i, x in enumerate(xs):
        if last is None:
            gap = x - 1
        else:
            gap = x - last - 1
        vx.append((x, i + 1, gap))
        last = x

    vy = []
    last = None
    for j, y in enumerate(ys):
        if last is None:
            gap = y - 1
        else:
            gap = y - last - 1
        vy.append((y, j + 1, gap))
        last = y

    h = len(vy) * 2
    w = len(vx) * 2
    dist = np.ones((h, w), dtype=np.int64)

    # apply x-gaps to odd x-columns (1-based -> 0,2,4,...)
    for idx, (_, rankx, gap) in enumerate(vx, start=1):
        dist[:, 2 * idx - 2] *= gap

    # apply y-gaps to odd y-rows
    for jdx, (_, ranky, gap) in enumerate(vy, start=1):
        dist[2 * jdx - 2, :] *= gap

    # map original points to compressed coords (even indices: 2*rank)
    rankx_map = {x: r for x, r, _ in vx}
    ranky_map = {y: r for y, r, _ in vy}
    pts2 = []
    for idx, (x, y) in enumerate(points):
        cx = 2 * rankx_map[x]
        cy = 2 * ranky_map[y]
        pts2.append((cx, cy, idx + 1))  # keep 1-based id if needed

    return dist, pts2

def draw_borders(h, w, pts2):
    borders = np.zeros((h, w), dtype=np.int8)
    n = len(pts2)
    for i in range(n):
        x1, y1, _ = pts2[i]
        x2, y2, _ = pts2[(i + 1) % n]
        # convert 1-based-like coords to 0-based indices
        y_start, y_end = sorted((y1 - 1, y2 - 1))
        x_start, x_end = sorted((x1 - 1, x2 - 1))
        borders[y_start:y_end + 1, x_start:x_end + 1] = 1
    return borders

def flood_fill_outside(borders):
    bh, bw = borders.shape
    pad = 2

    b = np.zeros((bh + 2 * pad, bw + 2 * pad), dtype=np.int8)
    b[pad:pad + bh, pad:pad + bw] = borders

    # seed outside
    b[1, 1] = -1

    changed = True
    while changed:
        changed = False
        nb = b.copy()
        for i in range(1, nb.shape[0] - 1):
            for j in range(1, nb.shape[1] - 1):
                if nb[i, j] == 0:
                    if (nb[i - 1, j] == -1 or
                        nb[i + 1, j] == -1 or
                        nb[i, j - 1] == -1 or
                        nb[i, j + 1] == -1):
                        nb[i, j] = -1
                        changed = True
        b = nb

    # remove padding
    b = b[pad:pad + bh, pad:pad + bw]
    return b

def sum_rect(mat, x1, x2, y1, y2):
    # inputs are compressed coords (1-based even); convert to 0-based indices
    x_lo = min(x1, x2) - 1
    x_hi = max(x1, x2) - 1
    y_lo = min(y1, y2) - 1
    y_hi = max(y1, y2) - 1
    return mat[y_lo:y_hi + 1, x_lo:x_hi + 1].sum()

def main():
    points = read_points()

    dist_grid, pts2 = build_compressed_grid(points)
    h, w = dist_grid.shape

    borders = draw_borders(h, w, pts2)
    outside = flood_fill_outside(borders)

    # inside (red+green): tiles = pmin(borders, 0) + 1 in R logic
    # here: outside == -1, border == 1, interior == 0
    # pmin(borders,0)+1 on (border/outside/inside) is 1 for border/inside, 0 for outside
    tiles = np.minimum(outside, 0) + 1
    tiled_dist = tiles.astype(np.int64) * dist_grid

    n = len(pts2)

    # Part 1: largest rectangle area using all tiles (dist_grid)
    max1 = 0
    for i in range(n):
        x1, y1, _ = pts2[i]
        for j in range(i + 1, n):
            x2, y2, _ = pts2[j]
            area = sum_rect(dist_grid, x1, x2, y1, y2)
            if area > max1:
                max1 = area

    # Part 2: largest rectangle where area == tiled_area (only red/green)
    max2 = 0
    for i in range(n):
        x1, y1, _ = pts2[i]
        for j in range(i + 1, n):
            x2, y2, _ = pts2[j]
            area = sum_rect(dist_grid, x1, x2, y1, y2)
            tiled_area = sum_rect(tiled_dist, x1, x2, y1, y2)
            if area == tiled_area and area > max2:
                max2 = area

    print("Part 1:", max1)
    print("Part 2:", max2)

if __name__ == "__main__":
    main()