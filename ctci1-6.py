'''
STRING COMPRESSION

implement a method to perform basic string compression using the counts of repeated characters. 

e.g aabcccccaaa => a2b1c5a3

if compressed string is not smaller than original return original

--- 
methodology:
utilize 2 pointers and a counter (min 1) to iterate through string in O(n) complexity and O(1) space
'''

def stringCompression(string):
	iter1 = 0
	iter2 = 1
	count = 1
	answer = ""

	while iter2 < len(string):
		if string[iter2] == string[iter1]:
			iter2 += 1
			count += 1

		else:
			answer += string[iter1]
			answer += str(count)
			iter1 = iter2
			iter2 += 1
			count = 1

	answer += string[iter1]
	answer += str(count)

	if len(answer) > len(string):
		print string

	else:
		print answer 

test1 = "aabcccccaaa"
test2 = "aab"

stringCompression(test1)
stringCompression(test2)