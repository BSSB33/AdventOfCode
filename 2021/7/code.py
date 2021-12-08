from datetime import datetime

def parse_data(path):
    f = open(path, "r")
    return [int(n) for n in f.readline().split(",")]

def calculateOptimalPlane(data, task2) -> int:
    max_depth = max(data)
    min_fuel_cost = 100000000
    best_depth = 0
    for depth in range(0, max_depth):
        #print("{:.2f}%".format(depth / max_depth * 100))
        fuel_cost = 0
        for i in range(0, len(data)):
            fuel_cost += caluclate_individual_fuel_cost(task2, data[i], depth)
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            best_depth = depth
    return min_fuel_cost, best_depth

def caluclate_individual_fuel_cost(task2, ship_depth, target_depth):
    if not task2: return abs(ship_depth - target_depth)
    elif task2:
        fuel_cost = 0
        for i in range(1, abs(ship_depth - target_depth) + 1):
            fuel_cost += i
        return fuel_cost
            

if __name__ == "__main__":
    start = datetime.now()

    data = parse_data("input.txt")
    print(calculateOptimalPlane(data, False))
    print(calculateOptimalPlane(data, True))
    
    
    