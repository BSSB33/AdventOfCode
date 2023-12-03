"""One of the worsts code I have ever written at 10PM, TODO: Rewrite."""

import copy

def parse_data(path, explode=False):
    f = open(path, "r")
    data = []
    for line in f.read().split("\n"):
        data.append([c for c in line])
    # Adding a dot line to the beginning and end of the data
    #data.insert(0, ['.'] * len(data[0]))
    #data.append(['.'] * len(data[0]))
    return data

def get_neoughbouring_symbols(data, x, y, get_coordinates=False):
    """
    Returns a set of symbols (optionally with coordinates) that can be found around numbers.
    Only returns non numeric and non dot symbols.
    """
    symbols = []
    coordinates_to_try = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)]
    # print("Selected symbol: {}".format(data[x][y]))
    for x, y in coordinates_to_try:
        try:
            if data[x][y] != '.' and not data[x][y].isdigit():
                if get_coordinates:
                    symbols.append((data[x][y], (x, y)))
                else:
                    symbols.append(data[x][y])
        except IndexError:
            pass
    return symbols

def get_neoughbouring_numbers(data, x, y):
    number_coordintes = []
    coordinates_to_try = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)]
    # print("Selected symbol: {}".format(data[x][y])) # Should be a '*'
    for x, y in coordinates_to_try:
        try:
            if data[x][y].isdigit():
                number_coordintes.append((x, y))
        except IndexError:
            pass
    return number_coordintes

def get_coordinates_of_numberic_values(data):
    coordinates = []
    for x in range(0, len(data)):
        for y in range(0, len(data[x]) - 2):
            if data[x][y].isdigit() and data[x][y + 1].isdigit() and data[x][y + 2].isdigit():
                coordinates.append((int("".join([data[x][y], data[x][y+1], data[x][y+2]])),
                                    [(x, y), (x, y + 1), (x, y + 2)]))
                #print("Number found: {}".format(int("".join([data[x][y], data[x][y+1], data[x][y+2]]))))
                data[x][y] = '.'
                data[x][y + 1] = '.'
                data[x][y + 2] = '.'
    for x in range(0, len(data)):
        for y in range(0, len(data[x]) - 1):
            if data[x][y].isdigit() and data[x][y + 1].isdigit():
                coordinates.append((int("".join([data[x][y], data[x][y+1]])),
                                    [(x, y), (x, y + 1)]))
                #print("Number found: {}".format(int("".join([data[x][y], data[x][y+1]]))))
                data[x][y] = '.'
                data[x][y + 1] = '.'
    for x in range(0, len(data)):
        for y in range(0, len(data[x])):
            if data[x][y].isdigit():
                coordinates.append((int("".join(data[x][y])),
                                    [(x, y)]))
                #print("Number found: {}".format(int("".join(data[x][y]))))
                data[x][y] = '.'
    return coordinates
    

def reduce_stars(neighbours: list):
    star_coordinates = set()
    for symbol, coords in neighbours:
        if symbol == '*':
            star_coordinates.add(coords)
    return star_coordinates


def task1(data):
    coordinates = get_coordinates_of_numberic_values(copy.deepcopy(data))
    counting_numbers = []
    for number, coordinates in coordinates:
        numbers = set()
        for x, y in coordinates:
            if get_neoughbouring_symbols(data, x, y):
                numbers.add(int(number))
        counting_numbers.extend(list(numbers))
    return sum(counting_numbers)


def task2(data):
    coordinates_of_numeric_values = get_coordinates_of_numberic_values(copy.deepcopy(data))
    star_coordinates = set()
    for number, coordinates in coordinates_of_numeric_values:
        for x, y in coordinates:
            # symbols and coordinates of star characters know to have numeric neighbours
            neighbours = get_neoughbouring_symbols(data, x, y, get_coordinates=True)
            for star in reduce_stars(neighbours):
                star_coordinates.add(star)
    #print("Stars: ", star_coordinates)

    numbers_related_to_star = []
    for x, y in star_coordinates:
        # coordinates of numbers the star is related to
        found = get_neoughbouring_numbers(data, x, y)
        numbers_related_to_star.append(found)
    #print(numbers_related_to_star)

    result = 0
    for cog in numbers_related_to_star:
        numbers_to_multiply = set()
        # A cog really is a set of number digit coordinates 
        for x, y in cog:    
            # get numbers from coordinates (e.g.: we have a coordinate that belongs to a 4, and resolve it to 341)
            for number, coordinates in coordinates_of_numeric_values:
                if (x, y) in coordinates:
                    numbers_to_multiply.add(number)
        # print(numbers_to_multiply)
        if len(numbers_to_multiply) > 1:
            result += (numbers_to_multiply.pop() * numbers_to_multiply.pop())
    return result


if __name__ == "__main__":
    
    data = parse_data("input.txt")
    print(task1(data))
    print(task2(data))
