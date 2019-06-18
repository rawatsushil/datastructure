"""
Give an algo for shuffling deck of cards
"""
import random

class Shuffle:
	def __init__(self, arg):
		self.data = arg

	def shuffle_cards(self):
		max = len(self.data)-1

		while(max>0):
			r = random.randint(0, max)
			self.data[max], self.data[r] = self.data[r], self.data[max]
			max -= 1
		

if __name__ == '__main__':
	data = range(1, 53)
	sh = Shuffle(data)
	sh.shuffle_cards()
	print (sh.data)
		