import time

def resolve(source, mappings):
    # seed 79
    # seed-to-soil map:
    # 50 98 2
    # 52 50 48

    for dest, start, range in mappings:
        end = start + range
        if start <= source <= end:
            diff = source - start
            return dest + diff
    return source


def parse_data(path):
    f = open(path, "r")
    seeds = [int(n) for n in f.readline().strip().split(": ")[1].split(" ")]

    mappings = {}
    data = f.read()
    data = [line.strip() for line in data.split("\n") if line.strip() != ""]
    values = []
    key = ""
    for line in data:
        if line[0].isalpha():
            key = line.split(" ")[0]
            values = []
        else:
            values.append([int(n) for n in line.split(" ")])
        mappings[key] = values
    return seeds, mappings


def task1(seeds, mappings):
    locations = [] # Final numbers
    for seed in seeds:
        # print("Processing Seed: ", seed)
        for mapping in mappings.keys():
            # print(mappings[mapping])
            seed = resolve(seed, mappings[mapping])
            # print("Resolved Seed: ", seed)
        locations.append(seed)
    return min(locations)
    

if __name__ == "__main__":    
    start_time = time.time()

    seeds, mappings = parse_data("input.txt")
    # print(seeds, mappings)
    print(task1(seeds, mappings))
    #print(task2(seeds, mappings))

    print("--- %s seconds ---" % (time.time() - start_time))