import sys

if len(sys.argv) < 2:
	print("Usage: python day1.py <input file>")
	exit(1)

file = open(sys.argv[1], "r")

lines = file.readlines()
file.close()

sum = 0
for line in lines:
	val = 0
	for char in line:
		if char.isdigit():
			val = 10 * int(char)
			break
	for char in line[::-1]:
		if char.isdigit():
			val += int(char)
			break
	sum += val
 
print(f"Solution to the first part is {sum}")

sum = 0
digists_spelled	= ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in lines:
	val = 0
	break_ = False
	for i in range(len(line)):
		if break_:
			break
		if line[i].isdigit():
			val = 10 * int(line[i])
			break_ = True
			break
		else:
			for j in range(len(digists_spelled)):
				if digists_spelled[j] in line[0:i+1]:
					val = 10 * (j + 1)
					break_ = True
					break
	break_ = False
	for i in range(len(line)-1, -1, -1):
		if break_:
			break
		if line[i].isdigit():
			val += int(line[i])
			break_ = True
			break
		else:
			for j in range(len(digists_spelled)):
				if digists_spelled[j] in line[i:len(line)]:
					val += (j + 1)
					break_ = True
					break
	sum += val

print(f"Solution to the second part is {sum}")

