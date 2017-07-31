'''
CHECK PERMUTATION

given two strings, write a method to decide if one is a permutation of the other

---
methodology:
sort the strings, and do a compare -- python's default sort is quick sort
time complexity is O(nlogn) and space complexity is O(1)

if we can't sort the strings, then create a dictionary and do a letter count
space complexity becomes O(n) in that case
'''

def checkPermutation(string1, string2):
	string1.sort().lower()
	string2.sort().lower()

	if string1 == string2:
		return True

	return False

