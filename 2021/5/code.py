def parse_data(path):
    f = open(path, "r")
    return [n for n in f.read().split("\n")]

def create_grid(data):
    grid = []
    for line in data:
        directions = line.split(" -> ")
        pair_1 = (int(directions[0].split(",")[0]), int(directions[0].split(",")[1]))
        pair_2 = (int(directions[1].split(",")[0]), int(directions[1].split(",")[1]))
        pair = [pair_1, pair_2]
        grid.append(pair)
    return grid

def establish_grid(grid, diagonals=False):
    result = {}
    for pair in grid:
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        
        if (x1 == x2):
            for y in range((min(y1, y2)), (max(y1, y2)) + 1):
                result[(x1, y)] = result.get((x1, y), 0) + 1
        elif (y1 == y2):
            for x in range((min(x1, x2)), (max(x1, x2)) + 1):
                result[(x, y1)] = result.get((x, y1), 0) + 1
        elif diagonals:
            length = abs(x1 - x2)
            dx = (x2 - x1) / length
            dy = (y2 - y1) / length
            for n in range(length + 1):
                x = x1 + (dx * n)
                y = y1 + (dy * n)
                result[(x, y)] = result.get((x, y), 0) + 1
    return result

def calculate_intersections(grid, diagonals=False):
    return len([1 for v in establish_grid(grid, diagonals).values() if v > 1])

if __name__ == "__main__":
    data = parse_data("input.txt")
    grid = create_grid(data)
    
    print("V-H Intersections greater then 1: ", calculate_intersections(grid))
    print("D Intersections greater then 2: ", calculate_intersections(grid, True))