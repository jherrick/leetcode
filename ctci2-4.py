'''
PARTITION

write code to partition a linked list around a value x, s.t. all nodes less than x come before all nodes greater than or equal to x.
If x is contained within the list, the values of x only need to be after teh elements less than x. The partition element x can appear anywhere
in the "right partition"; it does not need to appear between the left and right partitions

---

methodology:
iterate through the linked list, and for each node, if the value is less than x, insert it at the head of the list -- else, insert it at the tail of the list
'''

def Partition(node, x):
	head, tail = node, node

	while node != None: 
		next = node.next
		if node.data < x:
			node.next = head
			head = node

		else:
			tail.next = node
			tail = node 

	tail.next = None 

	return head 

