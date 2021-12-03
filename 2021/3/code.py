def parse_data(path):
    f = open(path, "r")
    return [n for n in f.read().split("\n")]

def calculateColumn(data, column):
    n = len(data)
    ones = 0
    for i in range(0, n):
        if int(data[i][column:column+1]) == 1: ones += 1
    val = 1 if ones > (n-ones) else 0
    return ones, (n-ones), val, 1 - val

def calculate(data):
    gamma = ""
    epsilon = ""
    for i in range(0, len(data[0])):
        ones, zeros, first, second = calculateColumn(data, i)
        gamma += str(first)
        epsilon += str(second)
    return int(gamma, 2), int(epsilon, 2), int(gamma, 2) * int(epsilon, 2)
    
def calculate2(data, inverted):
    n = len(data[0])
    for i in range(0, n):
        ones, zeros, first, second = calculateColumn(data, i)
        if inverted: ones, zeros = zeros, ones

        if zeros > ones: keep = 0           
        elif ones > zeros: keep = 1
        elif ones == zeros:
            if inverted: keep = 0
            else: keep = 1
        if len(data) != 1:
            data = [item for item in data if int(item[i:i+1]) == keep]
    return int(data[0], 2)

if __name__ == "__main__":
    data = parse_data("input.txt")
    print(calculate(data))
    print(calculate2(data, False) * calculate2(data, True))