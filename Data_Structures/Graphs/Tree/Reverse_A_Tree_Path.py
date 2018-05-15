class Solution:
	def reversePathRecur(self, root, data, temp ,level, nextpos):
		if root is None:
			return None
		if root.data == data:
			root.data, temp[level] = temp[nextpos], root.data
			nextpos += 1
			return root

		temp[level] = root.data

		left = self.reversePathRecur(root.left, data, temp, level + 1, nextpos)
		if left == None:
			right = self.reversePathRecur(root.left, data, temp, level + 1, nextpos)
		if left or right:
			root.data = temp[nextpos]
			nextpos += 1
			return right if right else left
		return None

	def reversePath(self, root, data):
		temp = {}
		nextpos = 0
		level = 0
		self.reversePathRecur(root, data, temp, level , nextpos)
		inOrder(root)

class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.right = right
		self.left = left

def makeTree(array, left, right):
	if left <= right:
		mid = (left + right) // 2
		n = Node(array[mid])
		n.left = makeTree(array, left, mid - 1)
		n.right = makeTree(array, mid + 1, right)
		return n

def make(array):
	n = len(array)
	return(makeTree(array, 0, n-1))

def inOrder(root):
	if root is None:
		return
	inOrder(root.left)
	print(root.data, end=" ")
	inOrder(root.right)


array = [1,2,3,4,5,6,7,8,9]
n = len(array)
tree = make(array)
# inOrder(tree)
s = Solution()
s.reversePath(tree, 4)
