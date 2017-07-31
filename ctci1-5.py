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
	if |len(string1)-len(string2)| > 1:
		return False

	p1 = 0
	p2 = 0
	diffs = 0

	