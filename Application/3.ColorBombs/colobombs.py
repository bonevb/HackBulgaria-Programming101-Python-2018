import sys

def countConnectedBomb():
	print('Enter your data and press Ctrl + D')
	data = sys.stdin.readlines()

	matrix = []

	for i in data:
		row = []
		for j in i:
			if j !='\n':
				row.append(j)
		matrix.append(row)

	rows = len(matrix)
	cols = len(matrix[0])

	xDirections = [ 0,0,-1,1,-1,1, 1,-1]
	yDirections = [-1,1, 0,0,-1,1,-1, 1]

	def findBomb(matrix, color):
			count = 0
			for i in range(rows):
				for j in range(cols):
					if matrix[i][j] == color:
						getNeighbours(matrix, i, j, color)
						count += 1

			return count


	def getNeighbours(matrix, row, col, color):
		if row < 0 or row >= rows or col < 0 or col >= cols:
			return
		if  matrix[row][col] != color:
			return

		matrix[row][col] = 'X'
		for i in range(8):
			getNeighbours(matrix, row + xDirections[i], col + yDirections[i], color)


	a = findBomb(matrix, 'R')
	b = findBomb(matrix, 'B')
	c = findBomb(matrix, 'G')

	return a + b + c

#print(countConnectedBomb())
