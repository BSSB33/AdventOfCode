def parse_data(path):
    f = open(path, "r")
    data = f.read().split("\n")
    return data

def get_game_value(game, return_matches = False):
    game = game.split(': ')[1].split(' | ')
    your_numbers = [int(n) for n in game[0].split(' ') if n != '']
    winning_numbers = [int(n) for n in game[1].split(' ') if n != '']
    game_value = 1
    matches = 0
    for number in your_numbers:
        if number in winning_numbers:
            game_value *= 2
            matches += 1
    game_value = 0 if game_value == 1 else int(game_value / 2)
    return matches if return_matches else game_value

def task1(data):
    solution = 0
    for game in data:
        game_value = get_game_value(game)
        solution += game_value
    return solution

def task2(data):
    game_counter = {i: 1 for i in range(0, len(data))}
    for i in range(0, len(data)):
        game_value = get_game_value(data[i], True)
        if game_value > 0:
            for j in range(0, game_counter[i]):
                for game_id in range(i+1, i+1+game_value):
                    game_counter[game_id] += 1
    return sum(game_counter.values())


if __name__ == "__main__":
    data = parse_data("input.txt")
    #print(data)
    print(task1(data))
    print(task2(data))