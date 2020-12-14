def getNext(data, current, diff):
	values = []
	for i in range(0, len(data)):
		if data[i] <= current + 3 and data[i] >= current:
			values.append(data[i])
	#print(values)
	if data[0] - current == 1:
		diff[0] += 1
	else:
		diff[1] += 1
	current = data[0]
	data.remove(data[0])
	return current, diff

def simulate(data, current, diff, target):
	while current + 3 != target:
		current, diff = getNext(data, current, diff)
	diff[1] += 1

def countRoutes(data):
	route_lengths = {0: 1}
	for joltage in data:
		counter = 0
		for n in [1, 2, 3]:
			counter += route_lengths.get(joltage - n, 0)
		route_lengths[joltage] = counter
	biggest = max(data)
	return route_lengths[biggest]

if __name__ == "__main__":
	f = open("input.txt", "r")
	data = [int(n) for n in f.read().split("\n")]
	data.sort()

	current = 0
	target = max(data) + 3
	diff = [0, 0]

	# print(diff)
	simulate(data, current, diff, target)
	print("Part 1:", diff[0] * diff[1])

	f = open("input.txt", "r")
	data = [int(n) for n in f.read().split("\n")]
	data.sort()
	print("Part 2:", countRoutes(data))