# Given a staircase and give you can take 1 or 2 steps at a time, how many ways you can reach nth step.

class StairCase:
	def __init__(self, steps):
		self.steps = steps
		self.step_arr = []

	def find_steps(self):
		self.step_arr.append(1)
		self.step_arr.append(2)
		for i in range(2, self.steps):
			self.step_arr.append(self.step_arr[i-2]+self.step_arr[i-1])
		return self.step_arr[self.steps-1]



if __name__ == '__main__':
	s = StairCase(5)
	print (s.find_steps())
