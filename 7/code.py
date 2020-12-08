def read_and_parese_input(path):
	f = open(path, "r")
	data = f.read().strip().split('\n')

	bags1 = dict()
	bags2 = dict()

	for d in data:
		line = d.replace(',', '').replace('.', '').split()
		key = line[0] + '_' + line[1]
		bags1[key] = []
		bags2[key] = []
		for i in range(4, len(line)):
			if line[i] == 'bag' or line[i] == 'bags':
				name = line[i - 2] + '_' + line[i - 1]
				bags1[key].append(name)
				
				#For part2
				if name != 'no_other':
					for j in range(0, int(line[i - 3])):
						bags2[key].append(line[i - 2] + '_' + line[i - 1])
	return bags1, bags2

def count_bags(bags, contents):
    cnt = 0
    for bag in contents:
        if bag == 'no_other':
            continue
        else:
            cnt += 1
            cnt += count_bags(bags, bags[bag])

    return cnt

def check_bag(bags, contents):
    for bag in contents:
        if bag == 'no_other':
            continue
        elif bag == 'shiny_gold':
            return True
        else:
            if check_bag(bags, bags[bag]):
                return True
            else:
                continue
    return False

def count_part1(bags1):
	counter = 0
	for bag in bags1:
		if check_bag(bags1, bags1[bag]):
			counter += 1
	return counter

def count_part2(bags2):
	counter = 0
	counter += count_bags(bags2, bags2['shiny_gold'])
	return counter


bags1, bags2 = read_and_parese_input("input.txt")
print(f'Part 1: {count_part1(bags1)}')
print(f'Part 2: {count_part2(bags2)}')