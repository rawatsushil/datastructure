"""
docstring
"""
class Points:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class MinDistance:
	def __init__(self, points):
		self.points = sorted(points, key = lambda a: a.x)

	def find_min(self, points):
		if len(points) == 0:
			return 'Invalid string'
		elif len(points) == 1:
			return points[0]
		elif len(points) == 2:
			return (points[0], points[1])
		elif len(points) == 3:
			(a, b, c) = points
			ret = (a, b) if self.dis(a, b)<= self.dis(a, c) else (a, c)
			ret =  ret if self.dis(ret[0], ret[1]) <= self.dis(b, c) else (b,c)
			return ret
		else:
			mid = len(self.points)//2
			left_a, left_b = find_min(self.points[: mid])
			right_a, right_b = find_min(self.points[mid :])
			local_min = min(self.dis(left_a, left_b), dis(right_a, right_b))

			local_mid = left_b.x + right_b.x // 2
			mid_range = filter(lambda pt: pt.x >= mid -local_mid and pt.x <=mid +local_mid)
			mid_range = sorted(mid_range, key = lambda a : a,y)

			# for loop to dfind min distance and return

	def dis(self, point1, point2):
		return abs(((point1.x - point2.x)**2 + (point1.y -point2.y)**2)**0.5)
		


if __name__ == '__main__':
	points = [
		Points(1, 2), Points(0, 0), Points(3, 6), Points(4, 7),
		Points(5, 5), Points(8, 4), Points(2, 9), Points(4, 5)
	]
	minimum = MinDistance(points)
	minimum.find_min(minimum.self.points)