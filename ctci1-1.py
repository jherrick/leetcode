'''
IS UNIQUE

implement an algo to determine if a str has all unique chars

variant: cannot use addtl data structs

---

methodology: corner case #1, if str (minus spaces) is longer than 26 chars return false

create data struct (dict/array) and at each letter check to see if it has already
been added -- if false, add it, if true, return FALSE 
time and space complexity are O(n) and O(1) respectively

for variant; still use corner case, but instead of data struct utilize 2 pointers
for each char, use 2nd pointer to check if another match exists (lower and upper)
this increases time complexity it n^2 but lowers space complexity to O(1)
'''

def isUnique(string):
	checker = {}

	for char in string:
		if char in checker:
			return False
		else:
			checker[char] = 0

	return True

def isUniqueVarient(string):
	p1 = 0

	while p1 < len(string):
		p2 = p1 + 1
		while p2 < len(string)
			if string[p1] == string[p2]:
				return False
			p2 += 1
		p1 += 1