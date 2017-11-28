'''
ONE AWAY

there are three types of edits that can be performed on strings: insert a char,
remove a char, or replace a char.  Given two strs, write a fx to check if they are 
one edit (or zero edits) away

EXAMPLE:
pale, ple -> True
pales, pale -> True
pale, bale -> True
pale, bake -> False

---
methodology:

corner case: if str lens differ by > 1 return false

two pointers, check each char allowing for one difference -- if str lens differ
delay pointer on shorter str upon finding first difference

O(1) space complexity, O(n) time complexity
'''

def oneAway(string1, string2):
	#check corner case of length differeing by > 1
	if |len(string1)-len(string2)| > 1:
		return False

	#find longer string
	if len(string1) > len(string2):
		s1 = string1
		s2 = string2
	else:
		s2 = string1
		s1 = string2

	#create pointers and flag
	iter1 = 0
	iter2 = 0
	foundDifference = False

	while iter2 < len(s2) and iter1 < len(s1):
		
		if s1[iter1] != s2[iter2]:
			if not foundDifference:
				return False
			foundDifference = True

		if len(s1) == len(s2):
			iter1 += 1

		else:
			iter1 += 1

		iter2 += 1

	return True 


	


	