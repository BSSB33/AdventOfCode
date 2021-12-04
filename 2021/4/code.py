def parse_data(path):
    tables = []
    table = []

    f = open(path, "r")
    numbers = f.readline()[:-1].split(",")
    input = [n for n in f.read()[1:].split("\n")]
    for element in input:
        if element == "":
            tables.append(table)
            table = []
        else: table.append(createDict(element))
    tables.append(table)

    f.close()
    return numbers, tables

def createDict(row):
    row = [item for item in row.replace("  ", " ").split(" ") if item != ""]
    new_row = dict()
    for element in row: 
        new_row[int(element)] = False
    return new_row

def getTable(tables, table_id):
    return tables[table_id]

def printTable(tables, table_id, numbers_only=False):
    print("Table " + str(table_id) + ":")
    for row in getTable(tables, table_id):
        if numbers_only: print(row.keys())
        else: print(row)

def checkRowWin(table):
    counter = 0
    for row in table:
        for key in row.keys():
            if row[key]: counter += 1
            if counter == 5: return True
        counter = 0
    return False

def checkColumnWin(table):
    counter = 0
    for i in range(0, 5):
        for dic in table:
            if dic[list(dic.keys())[i]]:
                counter += 1
            if counter == 5: 
                return True
        counter = 0
    return False

def checkWin(table):
    return checkRowWin(table) or checkColumnWin(table)

def setValues(tables, number):
    for table in tables:
        for row in table: 
            for key in row:
                if key == number: row[key] = True
    return tables

def getWinningTable(numbers, tables):
    for i in range(len(numbers)):
        tables = setValues(tables, int(numbers[i]))
        for j in range(len(tables)):
            if checkWin(tables[j]):
                #print("Found winning table for number " + str(j+1), "last called number: ", numbers[i])
                #printTable(tables, j, False)
                return tables, j, int(numbers[i])

def calculateSum(tables, j):
    sum = 0
    for row in getTable(tables, j):
        for key in row:
            if not row[key]: sum += key
    return sum

def getWinningTable2(numbers, tables):
    n = len(tables)
    winning_tables = []
    for i in range(len(numbers)):
        tables = setValues(tables, int(numbers[i]))
        for j in range(len(tables)):
            if j not in winning_tables:
                if checkWin(tables[j]):
                    #print("Found winning table for number " + str(j+1))
                    winning_tables.append(j)
            if len(winning_tables) == n: return tables, j, int(numbers[i])

if __name__ == "__main__":
    numbers, tables = parse_data("input.txt")
    tables, j, last_called_number = getWinningTable(numbers, tables)
    sum = calculateSum(tables, j)
    print("Sum: " + str(sum), "Last called number: " + str(last_called_number), "Result: " + str(sum * last_called_number))

    tables, j, last_called_number = getWinningTable2(numbers, tables)
    sum = calculateSum(tables, j)
    print("Sum: " + str(sum), "Last called number: " + str(last_called_number), "Result: " + str(sum * last_called_number))