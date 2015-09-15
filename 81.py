
matrix_file = open("p081_matrix.txt")
matrix = [map(int, line.split(",")) for line in matrix_file]
sums = []

for y, row in enumerate(matrix):
	sums.append(row)
	for x, cell in enumerate(row):
		if x == 0 and y == 0:
			sums[x][y] = cell
		elif x == 0:
			sums[y][x] = sums[y-1][x] + cell
		elif y == 0:
			sums[y][x] = sums[y][x-1] + cell
		else:
			sums[y][x] = min(sums[y-1][x], sums[y][x-1]) + cell

print sums[-1][-1]		