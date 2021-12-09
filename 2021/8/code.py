def parse_data(path):
    #be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    f = open(path, "r")
    unique_patterns = []
    output_values = []
    for line in f:
        line = line.rstrip('\n').split(' | ')
        unique_patterns.append(line[0].split(" "))
        output_values.append(line[1].split(" "))
    return unique_patterns, output_values

def is_simple_digit(number_unput):
    return len(number_unput) in [2, 3, 4, 7]

def task1(output_values):
    counter = 0
    for record in output_values:
        for value in record:
            if is_simple_digit(value): counter += 1
    return counter


if __name__ == "__main__":

    unique_patterns, output_values = parse_data("input.txt")
    print(task1(output_values))

    
    
    