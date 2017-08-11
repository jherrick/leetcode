'''
SUM LISTS

you have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, st the 1's digit is at the head of the list. Write a
fx that adds the two numbers and returns the sum as a linked list.

---
methodology:

create a "carry" counter, and use two iterators to traverse the linked lists, summing and building 
the answer as you go

O(n) time complexity, O(1) space complexity
'''

def sumLists(l1, l2):
	head1, head2 = l1, l2
	carry = 0

	new = Node()

	while head1 and head2:
		temp = head1.data + head2.data

		if carry:
			temp += 1

		if temp > 10:
			temp = temp%10
			carry = 1

		else:
			carry = 0

		new.data = temp
		head1 = head1.next
		head2 = head2.next
		new.next = Node()
		new = new.next
