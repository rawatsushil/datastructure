#Given an array of positive number, find maximum sum 
#subsequence such that elements in this subsequence are not adjacent to each other.


class MaxSum:
	def __init__(self, arr):
		self.arr = arr
		self.size = len(self.arr)
		
	def calculate(self):
		if self.size == 0:
			return 'empty array'
		elif self.size == 1:
			return self.arr[0]
		else:
			self.arr[1]= max(self.arr[0], self.arr[1])
			for i in range(2, self.size):
				self.arr[i] = max(self.arr[i-1], self.arr[i]+self.arr[i-2])
			return self.arr[self.size-1]

if __name__ == '__main__':
	arr = [5, 5, 1, -1]
	ms = MaxSum(arr)
	print(ms.calculate())

