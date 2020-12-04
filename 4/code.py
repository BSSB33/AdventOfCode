import re

f = open("input.txt", "r")
data = f.read().split("\n")

list = []
newEntries = []
record = []
string = ""
data.append('')
for entry in data:
    line = entry.split(" ")
    if line[0] != '':
        string = string + " " + entry
    if line[0] == '':
        newEntries.append(string)
        string = ""
#print(newEntries)

for entry in newEntries:
    line = entry.split(" ")
    d = dict()
    d["cid"] = "missing"
    for attribute in line:
        splitted = attribute.split(":")
        if splitted[0] != "":
            key = splitted[0]
            value = splitted[1]
            d[key] = value
    list.append(d)
#print(list)

count = 0
passports = []
for entry in list:
    if len(entry) == 8:
        count = count + 1
        passports.append(entry)
print("Count of Valud passprts: " + str(count))

#*
countNew = 0
validatedPassports = []

for passport in passports:
    if len(passport["byr"]) == int(4) and int(passport["byr"]) >= int(1920) and int(passport["byr"]) <= int(2002):        
        if len(passport["iyr"]) == int(4) and int(passport["iyr"]) >= int(2010) and int(passport["iyr"]) <= int(2020):
            if len(passport["eyr"]) == int(4) and int(passport["eyr"]) >= int(2020) and int(passport["eyr"]) <= int(2030):
                if passport["hgt"][-2:] == "cm" or passport["hgt"][-2:] == "in":
                    size = ''.join(passport["hgt"].split())[:-2].upper()
                    if (passport["hgt"][-2:] == "cm" and int(size) >= int(150) and int(size) <= int(193)) or (passport["hgt"][-2:] == "in" and int(size) >= int(59) and int(size) <= int(76)):
                        pattern = re.compile("#[a-f0-9]+")
                        if passport["hcl"][0] == "#" and len(passport["hcl"]) == int(7) and pattern.fullmatch(passport["hcl"]) is not None: #issue?
                            if passport["ecl"] in ['amb', "blu", "brn", "gry", "grn", "hzl", "oth"]:
                                if len(passport["pid"]) == int(9):
                                    countNew = countNew + 1
                                    validatedPassports.append(passport)

print("Count of Valid passprts v2: " + str(countNew))
