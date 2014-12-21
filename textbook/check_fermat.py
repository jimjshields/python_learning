def check_fermat(a, b, c, n):
    if n > 2 and a**n == b**n + c**n:
        print "Fermat was wrong!"
    else:
        print "Fermat was right..."
        
a = int(raw_input("a?"))
b = int(raw_input("b?"))
c = int(raw_input("c?"))
n = int(raw_input("n?"))

check_fermat(a, b, c, n)
    