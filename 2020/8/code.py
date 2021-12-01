data = open('input2.txt').read().split('\n')
commands = []
accumulator = 0
for command in data:
	command = command.split(" ")
	commands.append([command[0], int(command[1]), False])

def stuff(commands, i, accumulator):
	print("i = " + str(i))
	if commands[i][0] == "nop":
		commands[i][2] = True
		i += 1

	elif commands[i][0] == "acc":
		commands[i][2] = True
		accumulator += int(commands[i][1])
		i += 1

	elif commands[i][0] == "jmp":
		commands[i][2] = True
		i += commands[i][1]
	return commands, i, accumulator

i = 0
while not commands[i][2]:
	commands[i][2] = True
	commands, i, accumulator = stuff(commands, i, accumulator)

print(accumulator)