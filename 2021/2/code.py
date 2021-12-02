def parse_data(path):
    f = open(path, "r")
    return [n for n in f.read().split("\n")]

def calculate(data):
    depth = 0
    forward = 0
    for command in data:
        command = command.split(" ")
        if command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
        elif command[0] == "forward":
            forward += int(command[1])
        
    return depth*forward
        
def calculate2(data):
    depth = 0
    forward = 0
    aim = 0
    for command in data:
        command = command.split(" ")
        if command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
        elif command[0] == "forward":
            forward += int(command[1])
            depth += aim * int(command[1])
        
    return depth*forward

if __name__ == "__main__":

    data = parse_data("input.txt")
    print(calculate(data))
    print(calculate2(data))