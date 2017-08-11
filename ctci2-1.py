'''
REMOVE DUPS

write code to remove duplicates from an unsorted linked list

variant: no temp buffer allowed

--- 
methodology:

store values in temp buffer and if you come upon a duplicate, dereference the pointers

O(n) time complexity, O(n) space complexity

variant:

utilize 2 pointers and for each value, check other values with 2nd pointer

O(n^2) time complexity, O(1) space complexity
'''

def removeDups(head):
	temp = []

	cur = head

	while cur:
		if cur.data not in temp:
			temp.append(cur.data)
		else:
			cur.prev = cur.next

		cur = cur.next

