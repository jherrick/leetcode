'''
RETURN KTH TO LAST

implement an algo to find the kth to last element of a singly linked list

---
methodology:

utilize 2 pointers, begin with p1 advancing forward k times, then begin with p2. when p1 is null, return p2

O(n) time complexity, O(1) space complexity
'''

def kthToLast(head):
	k = 5
	p1 = head
	p2 = head
	count = 0

	while p1:
		p1 = p1.next
		count += 1
		if count >= 5:
			p2 = p2.next

	return p2
