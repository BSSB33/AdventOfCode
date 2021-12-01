day1_data = open("input.txt", "r")
nums = [int(x.rstrip('\n')) for x in day1_data]

# Part 1
print(next(loop1 * loop2 for loop1 in nums for loop2 in nums if loop1 + loop2 == 2020))

# Part 2
print(next(loop1 * loop2 * loop3 for loop1 in nums for loop2 in nums for loop3 in nums if loop1 + loop2 + loop3 == 2020))

day1_data.close()