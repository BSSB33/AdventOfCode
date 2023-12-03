def parse_data(path, explode=False):
    f = open(path, "r")
    data = []
    for line in f.read().split("\n"):
        data.append([c for c in line])
    # Adding a dot line to the beginning and end of the data
    data.insert(0, ["."] * len(data[0]))
    data.append(["."] * len(data[0]))
    return data

def get_neoughbouring_symbols(data, x, y):
    """Only returns non numeric and non dot symbols."""
    symbols = []
    coordinates_to_try = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)]
    # print("Selected symbol: {}".format(data[x][y]))
    for x, y in coordinates_to_try:
        try:
            if data[x][y] != "." and not data[x][y].isdigit():
                symbols.append(data[x][y])
        except IndexError:
            pass
    return symbols

def get_coordinates_of_numberic_values(data):
    coordinates = []
    for x in range(0, len(data)):
        for y in range(0, len(data[x]) - 2):
            if data[x][y].isdigit() and data[x][y + 1].isdigit() and data[x][y + 2].isdigit():
                coordinates.append((int("".join([data[x][y], data[x][y+1], data[x][y+2]])),
                                    [(x, y), (x, y + 1), (x, y + 2)]))
                #print("Number found: {}".format(int("".join([data[x][y], data[x][y+1], data[x][y+2]]))))
                data[x][y] = "."
                data[x][y + 1] = "."
                data[x][y + 2] = "."
    for x in range(0, len(data)):
        for y in range(0, len(data[x]) - 1):
            if data[x][y].isdigit() and data[x][y + 1].isdigit():
                coordinates.append((int("".join([data[x][y], data[x][y+1]])),
                                    [(x, y), (x, y + 1)]))
                #print("Number found: {}".format(int("".join([data[x][y], data[x][y+1]]))))
                data[x][y] = "."
                data[x][y + 1] = "."
    for x in range(0, len(data)):
        for y in range(0, len(data[x])):
            if data[x][y].isdigit():
                coordinates.append((int("".join(data[x][y])),
                                    [(x, y)]))
                #print("Number found: {}".format(int("".join(data[x][y]))))
                data[x][y] = "."
    return coordinates
    

def task1(data):
    coordinates = get_coordinates_of_numberic_values(data)
    counting_numbers = []
    for number, coordinates in coordinates:
        numbers = set()
        for x, y in coordinates:
            if get_neoughbouring_symbols(data, x, y):
                numbers.add(int(number))
        counting_numbers.extend(list(numbers))
    #print(counting_numbers)
    return sum(counting_numbers)


if __name__ == "__main__":
    
    data_mini = parse_data("input_mini.txt")
    data = parse_data("input.txt")
    print(task1(data_mini))
    print(task1(data))

# Input data:
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
