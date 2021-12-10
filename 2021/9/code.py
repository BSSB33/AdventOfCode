import math

def parse_data(path):
    f = open(path, "r")
    return [[int(char) for char in line] for line in f.read().split("\n") if line]

def print_matrix(matrix):
    for line in matrix:
        print("".join([str(char) for char in line]))

def add_border_to_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([9] + matrix[i] + [9])
    new_matrix = [[9] * (len(matrix[0]) + 2)] + new_matrix + [[9] * (len(matrix[0]) + 2)]
    return new_matrix

def find_low_points(matrix):
    low_points = []
    risk_sum = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if matrix[i - 1][j] > matrix[i][j] and matrix[i + 1][j] > matrix[i][j] and matrix[i][j - 1] > matrix[i][j] and matrix[i][j + 1] > matrix[i][j]:
                low_points.append((i, j))
                risk_sum += matrix[i][j] + 1            
    return low_points, risk_sum

def find_basins_in_matrix(matrix, low_points):
    basins = []
    for point in low_points:
        if matrix[point[0]][point[1]] < 9:
            basins.append(find_basins(matrix, point[0], point[1]))
    return basins

def find_basins(matrix, x, y):
    basin = []
    if matrix[x][y] < 9:
        basin.append((x, y))
        matrix[x][y] = 9
        if matrix[x - 1][y] < 9:
            basin += find_basins(matrix, x - 1, y)
        if matrix[x + 1][y] < 9:
            basin += find_basins(matrix, x + 1, y)
        if matrix[x][y - 1] < 9:
            basin += find_basins(matrix, x, y - 1)
        if matrix[x][y + 1] < 9:
            basin += find_basins(matrix, x, y + 1)
    return basin

def calculate_results(basins):
    sizes = []
    for basin in basins:
        sizes.append(len(basin))
    sizes.sort(reverse=True)
    return math.prod(sizes[0:3])

if __name__ == "__main__":

    data = parse_data("input.txt")
    data = add_border_to_matrix(data)
    low_points, risk_sum = find_low_points(data)
    print("Risk sum:", risk_sum)
    result = calculate_results(find_basins_in_matrix(data, low_points))
    print("Result:", result)