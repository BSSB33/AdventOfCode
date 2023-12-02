def parse_data(path, explode=False):
    f = open(path, "r")
    return [n for n in f.read().split("\n")]
    
        

def task1(data):
    possible_games = {game.split(":")[0][5:] for game in data}
    limits = {"red": 12, "green": 13, "blue": 14}

    for game in data:
        game_id, game_data = game.split(":")[0][5:], game.split(":")[1]

        for reveal in game_data.split(";"):
            reveals = [r.split(" ") for r in reveal[1:].split(", ")]
            
            for num, color in reveals:
                if int(num) > limits[color] and game_id in possible_games:
                    possible_games.remove(game_id)

    return sum(int(game_id) for game_id in possible_games)

        
def task2(data):
    solution = 0

    for game in data:
        minimums = {"red": 0, "green": 0, "blue": 0}
        game_data = game.split(":")[1]

        for reveal in game_data.split(";"):
            reveals = [r.split(" ") for r in reveal[1:].split(", ")]
            for num, color in reveals:
                num = int(num)
                if num > minimums[color]:
                    minimums[color] = num

        solution += minimums["red"] * minimums["green"] * minimums["blue"]

    return solution


if __name__ == "__main__":
    
    data = parse_data("input.txt")
    print(task1(data))
    print(task2(data))
