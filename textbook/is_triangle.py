def is_triangle(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    
    if (a + b < c) or (a + c < b) or (c + b < a):
        print "It is not a triangle!!!!"
    else:
        print "We've got a triangle!!!!"

a = raw_input("a?")
b = raw_input("b?")
c = raw_input("c?")

is_triangle(a, b, c)