'''
ZERO MATRIX

write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

---
methodology:
create 2 arrays representing x and y coords in the matrix and set 0s based on array indices -- this avoids "zeroing out"
entire matrix and allows O(n) time compexity and O(1) space complexity"

'''

def zeroMatrix(matrix):
	xArray = [1 for x in range(len(matrix[0]))]
	yArray = [1 for y in range(len(matrix))]

	result = [[1 for x in range(len(matrix[0]))] for y in range(len(matrix))]

	for y in range(len(yArray)):
		for x in range(len(xArray)):
			if matrix[y][x] == 0:
				xArray[x] = 0
				yArray[y] = 0

	for y in range(len(yArray)):
		for x in range(len(xArray)):
			if yArray[y] == 0 or xArray[x] == 0:
				result[y][x] = 0
			else:
				result[y][x] = matrix[y][x]

	print "matrix"
	for x in matrix:
		print x

	print "result"
	for y in result:
		print y

test = [[1,2,0,4],[5,6,7,8],[9,10,11,12]]

zeroMatrix(test)


