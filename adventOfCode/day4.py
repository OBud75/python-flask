def part_1_solution(file_name: str):
	graph = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			graph.append(line.strip())
			line = input_file.readline()

	rows, cols = len(graph), len(graph[0])
	ans = 0

	for i in range(rows):
		for j in range(cols):
			if graph[i][j] == "X":
				up = "".join(graph[x][j] for x in range(i, max(-1, i-4), -1))
				down = "".join(graph[x][j] for x in range(i, min(rows, i+4)))
				left = "".join(graph[i][x] for x in range(j, max(-1, j-4), -1))
				right = "".join(graph[i][x] for x in range(j, min(cols, j+4)))

				up_right = []
				x, y, loop_count = i, j, 0
				while x >= 0 and y < cols and loop_count < 4:
					up_right.append(graph[x][y])
					x -= 1
					y += 1
					loop_count += 1
				up_right = "".join(up_right)

				up_left = []
				x, y, loop_count = i, j, 0
				while x >= 0 and y >= 0 and loop_count < 4:
					up_left.append(graph[x][y])
					x -= 1
					y -= 1
					loop_count += 1
				up_left = "".join(up_left)

				down_left = []
				x, y, loop_count = i, j, 0
				while x < rows and y >= 0 and loop_count < 4:
					down_left.append(graph[x][y])
					x += 1
					y -= 1
					loop_count += 1
				down_left = "".join(down_left)

				down_right = []
				x, y, loop_count = i, j, 0
				while x < rows and y < cols and loop_count < 4:
					down_right.append(graph[x][y])
					x += 1
					y += 1
					loop_count += 1
				down_right = "".join(down_right)

				all_words = [up, down, left, right, up_left, up_right, down_left, down_right]
				ans += all_words.count("XMAS")

	return ans


def part_2_solution(file_name: str):
	graph = []

	with open(file_name) as input_file:
		line = input_file.readline()
		while line:
			graph.append(line.strip())
			line = input_file.readline()

	rows, cols = len(graph), len(graph[0])
	valid = ["MAS", "SAM"]
	ans = 0

	for i in range(rows):
		for j in range(cols):
			if graph[i][j] == "A" and 0 < i < rows - 1 and 0 < j < cols - 1:
				pos_diagonal = "".join([graph[i+1][j-1], graph[i][j], graph[i-1][j+1]])
				neg_diagonal = "".join([graph[i-1][j-1], graph[i][j], graph[i+1][j+1]])
				if pos_diagonal in valid and neg_diagonal in valid: ans += 1

	return ans


print(part_1_solution("sample.txt"))
print(part_1_solution("full.txt"))

print(part_2_solution("sample.txt"))
print(part_2_solution("full.txt"))

