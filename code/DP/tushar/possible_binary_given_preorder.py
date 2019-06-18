# Given an array that represents Preorder Traversal, 
# find all possible Binary Trees with the given Preorder traversal

class Possible_Binary_tree:
	def __init__(self, preorder):
		self.arr = preorder
		self.size = len(self.arr)
		self.count_list = []

	def find_count(self):
		self.count_list.append(1)
		self.count_list.append(1)
		for i in range(1, self.size):
			self.count_list.append(self.calculate(i))

	def calculate(self, total_nodes):
		val = 0
		temp_nodes = total_nodes
		while(temp_nodes>=0):
			val += self.count_list[temp_nodes]*self.count_list[total_nodes-temp_nodes]
			temp_nodes -= 1
		return val




if __name__ == '__main__':
	preorder = [10,11, 12, 13, 14] #[1, 1, 2]
	pbt = Possible_Binary_tree(preorder)
	pbt.find_count()
	print (pbt.count_list.pop())