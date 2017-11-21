'''
LOOP DETECTION

given a circular linked list, implement an algorithm that returns the node at the beginning of the loop

---
methodology:
rabbit and the tortoise method, relatively straightforward and O(n) time complexity with O(1) space complexity
'''

def loopDetection(head):
	iter1 = head
	iter2 = head.next

	while iter1 != iter2:
		iter1 = iter1.next
		iter2 = iter2.next.next

	iter2 = head

	while iter1 != iter2:
		iter1 = iter1.next
		iter2 = iter2.next

	return iter1