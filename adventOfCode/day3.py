import re

def part_1_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(line)
			line = input_file.readline()

	matches = []
	for line in input:
		match = re.findall(r'mul\([0-9]*,[0-9]*\)', line)
		matches.extend(match)

	res = 0
	for match in matches:
		numbers = match[4:len(match)-1]
		num1, num2 = numbers.split(",")
		res += (int(num1) * int(num2))

	return res

def part_2_solution(file_name: str):
	input = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			input.append(line)
			line = input_file.readline()

	matches = []
	for line in input:
		match = re.findall(r'mul\([0-9]*,[0-9]*\)|don\'t\(\)|do\(\)', line)
		matches.extend(match)

	res = 0
	on = True
	for match in matches:
		if match == "don't()": on = False
		elif match == "do()": on = True
		elif on:
			numbers = match[4:len(match)-1]
			num1, num2 = numbers.split(",")
			res += (int(num1) * int(num2))

	return res


print(part_1_solution("sample.txt"))
print(part_1_solution("full.txt"))

print(part_2_solution("sample2.txt"))
print(part_2_solution("full.txt"))
