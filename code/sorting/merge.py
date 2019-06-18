class MergeSort(object):

	def __init__(self, arr):
		self.arr = arr

	def sort(self, arr):
		if len(arr) > 1:
			mid = len(arr)//2
			L = arr[:mid]
			R = arr[mid:]
			self.sort(L)
			self.sort(R)

			i = j = k = 0
			while i < len(L) and j < len(R):
				if L[i] < R[j]:
					arr[k] = L[i]
					i += 1
				else:
					arr[k] = R[j]
					j +=1 
				k += 1

			while i < len(L):
				arr[k] = L[i]
				k += 1
				i += 1

			while j < len(R):
				arr[k] = R[j]
				k += 1
				j += 1
				
	def display(self, arr):
		print (arr)


if __name__ == '__main__':
	a = [ 0, 100, 9, 1 ]
	ms = MergeSort(a)
	ms.sort(a)
	ms.display(a)