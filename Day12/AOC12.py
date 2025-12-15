# day12_part1_fast.py

INPUT_FILE = "inputAOC12.txt"

def parse_input(path=INPUT_FILE):
    text = open(path, "r", encoding="utf-8").read().rstrip("\n")
    lines = text.splitlines()

    # Find split between shapes and regions: first "WxH:" line
    split_idx = None
    for i, line in enumerate(lines):
        s = line.strip()
        if "x" in s and s.endswith(":"):
            split_idx = i
            break
    shape_lines = lines[:split_idx]
    region_lines = lines[split_idx:]
    return shape_lines, region_lines

def compute_shape_areas(shape_lines):
    areas = []
    cur_idx = None
    cur_grid = []

    for line in shape_lines + [""]:
        s = line.strip()
        if not s:
            if cur_idx is not None:
                a = sum(row.count("#") for row in cur_grid)
                areas.append(a)
                cur_idx = None
                cur_grid = []
            continue
        if s.endswith(":") and s[:-1].isdigit():
            if cur_idx is not None:
                a = sum(row.count("#") for row in cur_grid)
                areas.append(a)
            cur_idx = int(s[:-1])
            cur_grid = []
        else:
            cur_grid.append(s)

    return areas

def count_fittable_regions(region_lines, areas):
    count = 0
    for line in region_lines:
        s = line.strip()
        if not s or ":" not in s:
            continue
        dims, rest = s.split(":", 1)
        dims = dims.strip()
        if "x" not in dims:
            continue
        W, H = map(int, dims.split("x"))
        counts = list(map(int, rest.strip().split()))
        total_present_area = sum(c * a for c, a in zip(counts, areas))
        if total_present_area <= W * H:
            count += 1
    return count

def main():
    shape_lines, region_lines = parse_input()
    areas = compute_shape_areas(shape_lines)
    ans = count_fittable_regions(region_lines, areas)
    print(ans)

if __name__ == "__main__":
    main()