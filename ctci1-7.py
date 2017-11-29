'''
ROTATE MATRIX

given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees

can you do it in place?

---
methodology:
swap each layer starting out and working in
'''

def rotate(matrix):
	#corner case no matrix or non-NxN matrix
	if len(matrix) == 0 or len(matrix) != len(matrix[0]):
		return False

	for x in range(len(matrix)/2):
		first = x
		last = len(matrix) - 1 - x
		for y in range(first, last):
			offset = y - first
			#save top in temp variable
			temp = matrix[first][y]
			#set left to top
			matrix[first][y] = matrix[last-offset][first]
			#set bottom to left
			matrix[last-offset][first] = matrix[last][last-offset]
			#set right to bottom
			matrix[last][last-offset] = matrix[y][last]
			#set top to right
			matrix[y][last] = temp 

	return True