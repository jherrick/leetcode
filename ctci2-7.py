'''
INTERSECTION

given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting

---
methodology:

seems to be an O(n!) complexity problem since iterating over both lists to obtain the values then requires us to
cross check the values against each other
'''