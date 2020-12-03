f = open("input.txt", "r")
data = f.read().split('\n')

def parseData(line):
    #2-8 t: pncmjxlvckfbtrjh
    line = line.split(' ')
    min = int(line[0].split('-')[0])
    max = int(line[0].split('-')[1])
    letter = line[1].replace(':', '')
    pw = line[2]
    return [min, max, letter, pw]

def makeList():
    list = []
    for i in range(0, len(data)-1):
        list.append(parseData(data[i]))
    return list

def countCorrectPw():
    list = makeList()
    correct = 0
    for i in range(0, len(list)):
        curr_count = list[i][3].count(list[i][2])
        if(curr_count >= list[i][0] and curr_count <= list[i][1]):
            correct = correct + 1
    return correct

print("Count of Correct PWs: " + str(countCorrectPw()))

def countNewCorrectPw():
    #2, 8, t, pncmjxlvckfbtrjh
    list = makeList()
    correct = 0
    for i in range(0, len(list)):
        if(list[i][2] == list[i][3][list[i][0]-1] or list[i][2] == list[i][3][list[i][1]-1]):
            correct = correct + 1
        if(list[i][2] == list[i][3][list[i][0]-1] and list[i][2] == list[i][3][list[i][1]-1]):
            correct = correct - 1
    return correct

print("Count of New Correct PWs: " + str(countNewCorrectPw()))