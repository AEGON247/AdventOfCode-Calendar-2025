import sys
import z3

def main():

    contents = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.readlines()
        lines = map(lambda x: x.strip(), lines)

        for line in lines:
            for entry in line.split(' '):
                contents.append(entry.strip())

    lights = []
    buttons = []
    cur_buttons = []
    joltages = []
    for entry in contents:

        if entry[0] == '[':
            light = set()
            for ind, c in enumerate(entry[1:-1]):
                if c == '#':
                    light.add(ind)

            lights.append(light)
        elif entry[0] == '(':
            button = tuple(map(int, entry[1:-1].split(',')))
            cur_buttons.append(button)
        elif entry[0] == '{':
            buttons.append(cur_buttons)

            joltage = list(map(int, entry[1:-1].split(',')))
            cur_buttons = []
            joltages.append(joltage)
        else:
            assert False



    '''
    for ind in range(len(lights)):
        print(lights[ind], end=' ')
        for entry in buttons[ind]:
            print(entry, end= ' ')
        print(joltages[ind])
        '''

    total = 0
    for ind in range(len(lights)):

        cur_buttons = buttons[ind]
        cur_joltage = joltages[ind]

        solver = z3.Optimize()
        variables = []
        joltages_var = [None] * len(cur_joltage)

        for name, button in enumerate(cur_buttons):
            var = z3.Int(str(name))

            variables.append(var)

            solver.add(var >= 0)


            for entry in button:
                if joltages_var[entry] is None:
                    joltages_var[entry] = var
                else:
                    joltages_var[entry] = joltages_var[entry] + var

        for jolt_int, entry in enumerate(cur_joltage):

            if joltages_var[jolt_int] is None:
                continue
            solver.add(cur_joltage[jolt_int] == joltages_var[jolt_int])


        total_presses = solver.minimize(sum(variables))

        if solver.check() == z3.sat:
            total += total_presses.value().as_long()
        else:
            assert False



    print(total)
    return

def calc_joltage(combo, len_target):

    res = [0] * len_target
    for entry in combo:
        for light in entry:
            res[light] += 1

    return res

def run_buttons(button_combos):
    res = set()

    for button_combo in button_combos:
        for button in button_combo:
            if button in res:
                res.remove(button)
            else:
                res.add(button)

    return res

if __name__ == '__main__':
    main()