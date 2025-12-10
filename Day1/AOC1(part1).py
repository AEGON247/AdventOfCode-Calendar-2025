# day1_part1.py
def solve(path="input.txt"):
    with open(path) as f:
        moves = f.read().strip().split()

    dial = 50
    count_zero = 0
    for mv in moves:
        d = mv[0]
        val = int(mv[1:])
        if d == "L":
            dial = (dial - val) % 100
        else:
            dial = (dial + val) % 100
        if dial == 0:
            count_zero += 1
    print(count_zero)

if __name__ == "__main__":
    solve()