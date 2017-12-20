'''
QUEUE VIA STACKS

implement a MyQueue class which implements a queue using two stacks

---
methodology:

'''

class Stack():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]


class MyQueue():
	def __init__(self):
		self.oldest = Stack()
		self.newest = Stack()

	def size():
		return len(self.oldest) + len(self.newest)

	def add(value):
		self.newest.push(value)

	def shiftStacks():
		if self.oldest.isEmpty():
			while not self.newest.isEmpty():
				self.oldest.push(self.newest.pop())

	def peek():
		shiftStacks()
		return self.oldest.peek()

	def remove():
		shiftStacks()
		return self.oldest.pop()

