import sys
import time
from tqdm import tqdm

def resolve(source, mappings):
    # seed 79
    # seed-to-soil map:
    # 50 98 2
    # 52 50 48

    for dest, start, range in mappings:
        if start <= source <= (start + range):
            return dest + (source - start)
    return source


def parse_data(path, seed_ranges=False):
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
    
    if seed_ranges:
        seed_pairs = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
        for beginning, _range in seed_pairs:
            print("Processing seed pair: ", (beginning, _range))
            for seed in tqdm(range(beginning, beginning+_range)):
                #print("Yielding: ", seed, mappings)
                yield seed, mappings
    else:
        return seeds, mappings


def process(part2=False):
    minimum = sys.maxsize
    for seed, mappings in parse_data("input_mini.txt", part2):
        for mapping in mappings.keys():
            seed = resolve(seed, mappings[mapping])
        if seed < minimum:
            minimum = seed
    return minimum
    

if __name__ == "__main__":    
    start_time = time.time()

    print(process())
    print(process(part2=True))

    print("--- %s seconds ---" % (time.time() - start_time))