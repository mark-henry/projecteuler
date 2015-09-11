size = 20

grid = [ [0] * size ] * size

def getgrid(row, col):
	if row < 0 or col < 0 or row >= size or col >= size:
		return 1
	return grid[row][col]

for row in range(0, size):
	for col in range(0, size):
		grid[row][col] = getgrid(row-1, col) + getgrid(row, col-1)

print grid[19][19]