from datetime import datetime

def parse_data(path):
    f = open(path, "r")
    return [int(n) for n in f.readline().split(",")]

# Slow version:
def simulate_lantern_fishes(data, days):
    for day in range(0, days):
        for i in range(0, len(data)):
            if data[i] == 0:
                data[i] = 6
                data.append(8)
            elif data[i] > 0:
                data[i] -= 1
    return sum(data)

# Faster version for part 2: 
# 1. Count different numbers in data
# 2. For every day and possible age of fish, shift array
# 3. Assign new value, create new fish
# 3. Sum all numbers
def simulate_immportal_lantern_fishes(data, days):
    fishes = [data.count(n) for n in range(9)]
    for day in range(days):
        mewFishes = [0] * 9
        for i in range(8):
            mewFishes[i] = fishes[i + 1]

        mewFishes[6] += fishes[0]
        mewFishes[8] = fishes[0]
        fishes = mewFishes

    return sum(fishes)

if __name__ == "__main__":
    start = datetime.now()

    data = parse_data("input.txt")

    print(simulate_lantern_fishes(data, 80))
    print(simulate_immportal_lantern_fishes(data, 256))

    end = datetime.now()
    print("Seconds:", (end - start).total_seconds())
