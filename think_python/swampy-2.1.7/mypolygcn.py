from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print(bob)

# def polygon(t, length, n):
# 
# """Draws a polygon with turtle t, segments of 
# given length, and n sides"""
# 
#     angle = 360.0/n
#     for i in range(n):
#         fd(t, length)
#         lt(t, angle)
# 
# polygon(bob, 50, 7)

def spiral(t, length, n):

    angle = 1
    
    for i in range(n):
        fd(t, length)
        lt(t, angle)
        angle = angle + .2

spiral(bob, 1, 1000)


wait_for_user()