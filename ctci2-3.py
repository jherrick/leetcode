'''
DELETE MIDDLE NODE

implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node

---
methodology:

set cur.data = next.data etc until cur.next is NULL, then delete cur.

O(n) time complexity, O(1) space complexity
'''

def deleteMiddleNode(node):

	cur = node

	while cur.next:
		cur.data = cur.next.data
		cur = cur.next

	cur.delete()
	#actually free up memory or just dereference the node