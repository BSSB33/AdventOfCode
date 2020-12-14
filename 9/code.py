#For input.txt use interval of [0, 24]
#For input2.txt use interval of [0, 4]
f = open("input.txt", "r")
data = [int(n) for n in f.read().split("\n")]

def increase(interval, next_index, amount = 1):
	interval[0] += amount
	interval[1] += amount
	next_index += amount
	return next_index

def getCurrNumbers():
	values = []
	for i in range(interval[0], interval[1] + 1):
		values.append(data[i])
	return values

def find2Numbers(arr, sum):
	s = set()
	for i in range(0, len(arr)):
		diff = int(sum) - int(arr[i])
		if arr[i] in s:
			return [arr[i], diff]
		s.add(diff)
	return [None, arr[i]]

def simulate(interval, next_index):
	while find2Numbers(getCurrNumbers(), data[next_index])[0] != None:
		#print(getCurrNumbers(), data[next_index], "->", str(find2Numbers(getCurrNumbers(), data[next_index])))
		next_index = increase(interval, next_index)
	return data[next_index]

#Algorithm from the internet :(
def subArraySum(arr, sum):
	for i in range(len(arr)):
		curr_sum = arr[i]
		j = i + 1
		while j <= len(arr):
			if curr_sum == sum:
				print(i, j-1)
				return [i, j-1]
			if curr_sum > sum or j == len(arr):
				break
			curr_sum = curr_sum + arr[j]
			j += 1
	return 0

def getValuesForPart2(arr, sum):
	bounds = subArraySum(arr, sum)
	values = []
	for i in range(bounds[0], bounds[1]):
		values.append(arr[i])
	return min(values) + max(values)

if __name__ == "__main__":
	interval = [0, 24]
	next_index = interval[1] + 1
	
	result = simulate(interval, next_index)
	print("Part 1 - Result:", result)
	print("Part 2 - Result:", getValuesForPart2(data, result))