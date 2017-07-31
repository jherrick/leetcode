'''
PALINDROME PERMUTATION

given a string, write a function to check if it is a permutation of a palindrome.
The palindrome does not need to be limited to just dict words

---
methodology

create a dict and do a letter count, if the str len is even all letters will be mults of 2
if the str len is odd, above is still true but one letter will have odd #.

O(n) time and space complexity
'''

import defaultdict

def palinedromePermuntation(string):
	checker = defaultdict

	for letter in string:
		checker[letter] += 1

	if len(string)%2 == 0:
		for item in checker:
			if checker[item]%2 != 0
				return False

	else:
		count = 0
		for item in checker:
			if checker[item]%2 != 0
				count += 1
				if count > 1:
					return False

	return True


	
