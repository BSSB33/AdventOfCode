import math

def parse_data(path):
    with open(path) as f:
        instructions = f.readline().strip()
        instructions = instructions.replace("L", "0").replace("R", "1")
        data = f.read().splitlines()[1:]
        maps = {}
        for line in data:
            line = line.split(" = ")
            maps[line[0]] = line[1][1:-1].split(", ")
        return instructions, maps
    
def task1(instructions, maps):
    steps = 0
    current = 'AAA'
    # 0 -> left, 1 -> right
    while current != 'ZZZ':
        instruction = int(instructions[steps % len(instructions)])
        current = maps[current][instruction]
        steps += 1
    return steps


def task2(instructions, maps):
    # This is the second approach I tried.
    # The usage of LCM was not straight forward.
    currents = [key for key in maps.keys() if key[-1] == 'A']
    lcm_result = 1
    step = 0

    while currents:
        new_currents = []
        for current in currents:
            if current.endswith('Z'):
                # Least common multiple
                lcm_result = math.lcm(lcm_result, step)
            else:
                instruction = int(instructions[step % len(instructions)])
                new_currents.append(maps[current][instruction])
        currents = new_currents
        step += 1

    return lcm_result


if __name__ == "__main__":
    instructions, maps = parse_data("input.txt")
    print(task1(instructions, maps))
    print(task2(instructions, maps))