# Given an array find longest increasing subsequence in this array.

class LIS(object):
	def __init__(self, arr):
		self.arr = arr
		self.final_arr = [1 for x in range(len(self.arr))]

	def find_longest_length(self):
		begin, end = 0, 1
		maxe = 1
		while(begin < end):
			if self.arr[begin] <= self.arr[end]:
				self.final_arr[end] = max(self.final_arr[begin]+ 1, self.final_arr[end])
				maxe  = max(maxe, self.final_arr[end])
			begin += 1

			if begin == end and begin != len(self.arr) - 1:
				begin, end = 0, end+ 1
		print (self.final_arr)
		return maxe 

if __name__ =='__main__':
	arr = [10, 22, 9, 33, 21, 50, 41, 60]
	lis = LIS(arr)
	print (lis.find_longest_length())
		
		