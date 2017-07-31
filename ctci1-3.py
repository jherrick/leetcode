'''
URLIFY

write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient
space at the end to hold the additional characters, and tha tyou are given the "true" length of the string. 

EXAMPLE: "Mr John Smith   ", 13 => "Mr%20John%20Smith"

---
methodology: 

iterate through string, incrementing count at each iteration -- if we find a 
space, replace it with '%20' -- end iteration when counter hits true length

O(n) time, O(1) space
'''

def urlify(string, length):
	count = 0
	answer = ""

	while count < length:
		if string[count] == " ":
			answer += "%20"
		else:
			answer += string[count]
		count += 1
	
