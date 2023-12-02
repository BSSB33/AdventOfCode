def parse_data(path, explode=False):
    f = open(path, "r")
    return [[*n] if explode else n for n in f.read().split("\n")]


def task1(data):
    solution = 0
    for line in data:
        first = None
        last = None

        for c in line:
            if c.isnumeric():
                if first is None:
                    first = int(c)
                else:
                    last = int(c)
        
        last = first if last is None else last
        merged = first * 10 + last
        solution += merged
    return solution



def task2(data):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = 0

    for line in data:
        first = None
        last = None

        for i,c in enumerate(line):
            if c.isnumeric():
                if first is None:
                    first = int(c)
                else:
                    last = int(c)

            for idx, number in enumerate(numbers):
                if line[i:].startswith(number):
                    if first is None:
                        first = idx+1
                    else:
                        last = idx+1

        last = first if last is None else last

        result += first * 10 + last
    return result

    
if __name__ == "__main__":
    # ["219", "8wo3", "abc123xyz", "x2ne34", "49872", "zight234", "7pqrstsixteen"]
    data = parse_data("input.txt")
    print(task1(data))
    print(task2(data))