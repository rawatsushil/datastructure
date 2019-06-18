# Given a min-heap of size n, find the kth least element in the min-heap.

class Heap:
	def __init__(self, h,  k):
		self.heap = h
		self.k = k
		self.size = len(h)


	def findKthsmallest(self):
		if self.size == 0:
			return 'empty array'
		
		while(self.k - 1):
			self.heap[0], self.heap[self.sizeze-1] = self.heap[self.size-1], self.heap[0]
			self.size -= 1
			self.k -= 1
			self.heapify(0, self.heap[0])
		return self.heap[0]

	def heapify(self, index, val):
		li = 2*index+1
		ri = 2*index+2


		if li <= self.size - 1:
			le = self.heap[li]
		else :
			return 

		if ri <= self.size - 1:
			re = self.heap[ri]
			if le < re and le < val:
				val, self.heap[li] = self.heap[li], val
				self.heapify(li, val)
			elif re < le and re < val:
				val, self.heap[ri] = self.heap[ri], val
				self.heapify(ri, val)

		elif le < val:
			le, val = val, le

	

if __name__ == '__main__':
	h = [10, 50, 40, 75, 60, 65, 45]
	k = 7
	heap = Heap(h, k)
	print(heap.findKthsmallest())
