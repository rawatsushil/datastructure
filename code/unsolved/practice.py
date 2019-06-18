class Sort():

	def partition(elements, low, high):
		total_length = len(elements)
		pivot_element = elements[high]
		index = low - 1

		for i in range(low, high):
			if elements[i] <= pivot_element:
				i += 1
				arr[i], arr[index] = arr[index], arr[i]

		return (i+1)



	def quick_sort(elements, low, high):
		if low <= high:
			index = self.partition(elements, low, high)
			quick_sort(elements, low, index-1)
			quick_sort(elements, index+1, high)


elements = [3, 1, 4, 5]
sort = Sort()
total = len(elements)
sort.quick_sort(elements, 0, total - 1)
