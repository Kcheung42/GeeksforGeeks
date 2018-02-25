
class MinHeap():
	def __init__(self):
		self.heap = []
		self.currentSize = 0

	def heapPush(self, value):
		self.heap.append(value)
		self.currentSize += 1
		self.heapifyUp(self.currentSize - 1)
		pass

	def heapPop(self):
		pop = self.heap[0]
		self.heap[0] , self.heap[self.currentSize - 1] = self.heap[self.currentSize - 1], self.heap[0]
		self.heapifyDown(0)

	def heapifyUp(self, i):
		parent = (i-1) // 2
		while parent >= 0:
			if self.heap[i] < self.heap[parent]:
				self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
			parent = (parent - 1) // 2

	def getSmallerChild(self, i):
		if 2 * i + 2 > self.currentSize - 1:
			return 2 * i + 1
		else:
			if self.heap[2 * i + 1] < self.heap[2 * i + 2]:
				return 2 * i + 1
			else:
				return 2 * i + 2

	def heapifyDown(self, i):
		while 2 * i + 1 <= self.currentSize - 1:
			smaller = self.getSmallerChild(i)
			if self.heap[smaller] < self.heap[i]:
				self.heap[smaller], self.heap[i] = self.heap[i], self.heap[smaller]
			i = smaller


h = MinHeap()
h.heapPush(9)
h.heapPush(8)
h.heapPush(7)
h.heapPush(23)
h.heapPush(2)
h.heapPush(12)
h.heapPush(22)
h.heapPush(25)
h.heapPop()

print(h.heap)
