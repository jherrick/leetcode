'''
INTERSECTION

given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting

---
methodology:

iterate over list1, storing values in dict as keys, then iterate over list2 checking if key exists in dict (constant time)

to do this in O(1) space, we can instead use two pointers to iterate over lists simultaneously, however our time complexity jumps to O(n!)
'''

import defaultdict

def intersection(list1, list2):
	head1 = list1
	head2 = list2

	temp = defaultdict

	while head1:
		defaultdict[head1] = 0
		head1 = head1.next

	while head2:
		if head2 in defaultdict:
			return True 
		head2 = head2.next

	return False 

