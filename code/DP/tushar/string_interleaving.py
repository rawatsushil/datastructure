class StringInterleaving:
	def __init__(self, s1, s2, s3):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.arr = [[0 for x in range(len(self.s2) +1)] for y in range(len(self.s1) +1)]

		self.make_matrix(self.arr)

	def make_matrix(self, arr):
		col_len = len(self.s2)
		row_len = len(self.s1)

		for i in range(0, row_len +1):
			for j in range(0, col_len +1):
				string_len = i+j
				if i == 0 and j == 0:
					arr[0][0] = 'T'
				elif i == 0 and (self.s2[j-1] == self.s3[string_len-1]):
					arr[i][j] = 'T'
				elif j == 0 and (self.s1[i-1] == self.s3[string_len-1]):
					arr[i][j] = 'T'
				elif (self.s2[j-1] == self.s3[string_len-1]) and (self.s1[i-1] == self.s3[string_len-1]):
					if arr[i-1][j] or arr[i][j-1] == 'T':
						arr[i][j] ='T'
				elif (self.s2[j-1] == self.s3[string_len-1]) and arr[i][j-1] =='T':
					arr[i][j] = 'T'
				elif (self.s1[i-1] == self.s3[string_len -1]) and arr[i-1][j] == 'T':
					arr[i][j] = 'T'

	def is_interleaved(self):
		return self.arr[len(self.s1)][len(self.s2)] == 'T'



if __name__ == '__main__':
	s1 = "YX"
	s2 = "X"
	s3 = "XXY"

	si = StringInterleaving(s1,s2,s3)
	print (si.is_interleaved())

