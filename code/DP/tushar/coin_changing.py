# Given coins of certain denominations and a total, how many ways these coins 
# can be combined to get the total.
class CoinChange:
	def __init__(self, arr, k):
		self.arr = arr
		self.k = k
		self.make_matrix(arr)

	def make_matrix(self, arr):
		self.matrix = [[0 for i in range(k+1)] for y in range (len(arr)+1)]

	def calculate(self):
		for i in range(len(self.arr)+1):
			for j in range(self.k+1):
				if j == 0:
					self.matrix[i][j] = 1
				elif i == 0 :
					self.matrix[i][j] = 0
				elif self.arr[i- 1] <= j:
					self.matrix[i][j] = self.matrix[i-1][j] + self.matrix[i][j-self.arr[i-1]]
				elif self.arr[i-1] > j:
					self.matrix[i][j] = self.matrix[i-1][j]
		return self.matrix[len(self.arr)][self.k]

if __name__ == '__main__':
	arr = [1, 2, 3]
	k = 5
	cc = CoinChange(arr, k)
	print (cc.calculate())
