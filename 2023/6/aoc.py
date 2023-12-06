def task(data):
    options_to_win = 1
    for time, distance in data:
        ways_to_win = 0
        for speed in range(1, time):
            if speed * (time - speed) > distance:
                ways_to_win += 1
        options_to_win *= ways_to_win
    return options_to_win


if __name__ == "__main__":    
    print(task([[7,9], [15,40],[30,200]]))
    print(task([[56, 334], [71, 1135], [79, 1350], [99, 2430]]))
    print(task([[71530, 940200]]))
    print(task([[56717999, 334113513502430]]))