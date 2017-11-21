'''
PALINDROME

implement a fx to check if a linked list is a palindrome

--- 
methodology:
assuming the list is not doubly linked and we only have access to the head, we'll need to iterate over the elements at least twice. In that circumstance, the problem is essentially identical identifying if an array is a palindrome
'''

def linkedListPalindrome(head):
	temp = []
	iter1 = 0
	iter2 = len(temp)-1

	cur = head

	while cur:
		temp.append(cur.data)
		cur = cur.next

	while iter1 != iter2:
		if temp[iter1] == temp[iter2]:
			iter1 += 1
			iter2 -= 1

		else:
			return False

	return True
