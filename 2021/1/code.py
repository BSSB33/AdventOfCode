def parse_data(path):
    f = open(path, "r")
    return [int(n) for n in f.read().split("\n")]

def count(data):
    counter = 0
    if data[0] < data[1]: counter += 1
    for i in range(1, len(data)):
        if data[i] > data[i-1]: counter += 1

    return counter

def count2(data):
    counter = 0
    for i in range(0, len(data)-3):
        if sum(data[i:i+3]) > sum(data[i-1:i+3-1]): counter += 1
    return counter

if __name__ == "__main__":

    data = parse_data("input.txt")
    print(count(data))
    print(count2(data))