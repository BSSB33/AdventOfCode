import numpy as np

with open("input.txt", 'r') as file:
    line_array = file.read().splitlines()
    map = [line.split() for line in line_array]
    save = [line.split() for line in line_array]

def getColLen():
    return np.shape(map)[0]

def extendMap():
    for x in range(0, getColLen()):
        map[x][0] = map[x][0] + save[x][0]

def getCount(X, Y):
    x = 0
    y = 0
    tree_count = 0
    while y <= getColLen() - 1:
        if(map[y][0][x] == "#"):
            tree_count = tree_count + 1
        if(x + X >= len(map[0][0])):
            extendMap()
        x = x + X
        y = y + Y

    print("Tree hit count for slope: x: " + str(X) + " y: " + str(Y) + " is -> " + str(tree_count))
    return(tree_count)

#Predefined values
arr = [[1,1], [3, 1], [5, 1], [7, 1], [1,2]]

sum = 1
for slope in arr:
    sum = sum * getCount(slope[0], slope[1])

print("Result: " + str(sum))