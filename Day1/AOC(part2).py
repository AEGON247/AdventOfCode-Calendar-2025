# day1_part2.py
def solve(path="input.txt"):
    with open(path) as f:
        moves = f.read().strip().split()

    total_passes = 0
    pos = 50
    for mv in moves:
        d = mv[0]
        val = int(mv[1:])
        step = 1 if d == "R" else -1
        for _ in range(val):
            pos = (pos + step) % 100
            if pos == 0:
                total_passes += 1
    print(total_passes)

if __name__ == "__main__":
    solve()