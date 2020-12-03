f = open("input.txt", "r")
expenses = f.read().split('\n')
expenses.pop()
list = []
for i in range(0, len(expenses)): 
    list.append(int(expenses[i]))
list.sort()

def hasArrayTwoMembersWithSum(array, size, sum):
    i = 0
    r = size-1
    
    while i < r:
        if (array[i] + array[r] == sum):
            return [array[i], array[r], array[i] * array[r]]
        elif (array[i] + array[r] < sum):
            i += 1
        else:
            r -= 1
    return 0 

print(hasArrayTwoMembersWithSum(list, len(list), 2020))


def find3Numbers(arr, size, sum): 
    for i in range( 0, size-2): 
        for j in range(i + 1, size-1):  
            for k in range(j + 1, size): 
                if arr[i] + arr[j] + arr[k] == sum: 
                    return [arr[i], arr[j], arr[k], arr[i] * arr[j] * arr[k]]
    return 0


print(find3Numbers(list, len(list), 2020))