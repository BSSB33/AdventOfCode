def parse_data(path):
    with open(path) as f:
        sequences = [[int(element) for element in line.split()] for line in f.read().splitlines()]
    return sequences


def build_diffrences(sequence):
    differences = [sequence]
    while not set(sequence) == {0}:
        sequence = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
        differences.append(sequence)
    return differences


def predict_next(sequence):
    differences = build_diffrences(sequence)
    differences[-1].append(0)
    for i in range(len(differences)-1, 0, -1):
        differences[i-1].append(differences[i][-1] + differences[i-1][-1])
    return differences[0][-1]


def predit_previous(sequence):
    differences = build_diffrences(sequence)
    differences[-1].insert(0, 0)
    for i in range(len(differences)-1, 0, -1):
        differences[i-1].insert(0, differences[i-1][0] - differences[i][0])
    return differences[0][0]


if __name__ == "__main__":
    sequences = parse_data("input.txt")
    print(sum(predict_next(sequence) for sequence in sequences))
    print(sum(predit_previous(sequence) for sequence in sequences))