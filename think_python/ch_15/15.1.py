import math

class Point(object):
	"""represents a point in 2-d space"""

p1 = Point()
p1.x = 4.0
p1.y = 5.0

p2 = Point()
p2.x = 10.0
p2.y = 9.0

def distance_bw_pts(p1, p2):
	distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
	return distance

print distance_bw_pts(p1, p2)