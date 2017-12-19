'''
STACK OF PLATES

imagine a stack of plates, if it gets too high, it might topple. Therefore, IRL we start a new stack when prev stack exceeds some threshold.

implement setOfStacks that mimics this.

it will be composed of several stacks and should create a new stack once prev exceeds capacity

---
methodology:
use a list of stacks and upon push/pop operations check if a stack needs to be added or removed from our list
'''

class StackList(maxSize):
	def __init__(self):
		self.list = []
		self.size = maxSize

	def push(number):
		last = self.list[-1]

		if last != None and len(last) < self.size:
			last.append(number)

		else:
			self.list.append([number])

	def pop():
		last = self.list[-1]

		result = last.pop()

		if len(last) == 0:
			self.list.pop()

		return result