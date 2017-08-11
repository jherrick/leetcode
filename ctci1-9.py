'''
STRING ROTATION

assume you have a method isSubstring which checks if one word is a substring of another

given two strings, s1 and s2, check if s2 is a rotation of s1 using only call to isSubstring

e.g. "waterbottle" is a rotation of "erbottlewat"

---

methodology:

append s2 to s2  creating s3 and call is substring of s1 and s3

example:

s1 = waterbottle
s2 = erbottlewat
s3 = erbottlewaterbottlewat

s3 contains the substring "waterbottle", therefore s2 is a rotation of s1

O(n) time complexity, O(1) space complexity
'''

def stringRotation(s1, s2):
	s3 = s2+s2

	if isSubstring(s1, s3):
		return True

	return False