# Given an array of integers where each element represents the max number of 
# steps that can be made forward from that element

class MinimumJumps():
	def __init__():
		self.steps = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9] #[1, 3, 2, 1, 1, 9]
		self.total_steps = len(self.steps)
	
	def calculate_jumps():
		if (self.total_steps == 0 or self.total_steps == 1):
			return 0
	
		minimum_steps, current_index = 1, 0
		end_reached = False
	
		while not end_reached:
			current_index = self.find_max_reach(current_index)
			if current_index != self.total_steps - 1
				minimum_steps += 1
		
		return minimum_steps
	
	def find_max_reach(current_index):
		current_index_value = self.steps[current_index]
		
		window_left = current_index + 1
		window_right = current_index + current_index_value

		max_index, max_reach = -1, -1
		
		if window.right >= self.total_steps:
			self.end_reached = True
			return self.total_steps

		for index in range(window_left, window_right + 1):
			if self.steps[index] + index >= max_value:
				max_index, max_reach = index, self.steps[index]+index
		