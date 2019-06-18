# Given an array that represents Inorder Traversal, 
# find all possible Binary Trees with the given Inorder traversal and print their preorder traversal

class PossibleBinaryTree:
	def __init__(self, arr):
		self.total_elements = len(arr)
		self.possible_tree_count = [1, 1, 2]

	def get_tree_count(self, tree_length):
		final_total = 0
		for index in range(0, tree_length):
			final_total += self.possible_tree_count[index]*self.possible_tree_count[tree_length-1-index]
		print (tree_length, final_total)
		return final_total

	def calculate_possible_trees(self):
		for index in range(2, self.total_elements):
			tree_length = index + 1
			self.possible_tree_count.append(self.get_tree_count(tree_length))
			print ('possible', self.possible_tree_count)

		return self.possible_tree_count.pop()

pt = PossibleBinaryTree([4, 5, 7, 8, 9])
print (pt.calculate_possible_trees())
