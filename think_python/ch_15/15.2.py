import math

class Point(object):
	"""point in 2d space"""

class Rectangle(object):
	"""represents a rectangle
	attributes: height, width, corner (all floats)
	"""

box = Rectangle()
box.height = 100.0
box.width = 50.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def move_rectangle(rectangle, dx, dy):
	rectangle.corner.x += dx
	rectangle.corner.y += dy


print '(%s, %s)' % (box.corner.x, box.corner.y)
move_rectangle(box, 10.0, 20.0)
print '(%s, %s)' % (box.corner.x, box.corner.y)
move_rectangle(box, 100.0, 20.0)
print '(%s, %s)' % (box.corner.x, box.corner.y)