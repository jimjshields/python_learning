def is_sorted(x):
    y = x[:]
    x.sort()
    if y == x:
        print True
    else:
        print False

is_sorted([1, 2, 3, 4, 5])
is_sorted([1, 2, 6, 2, 3, 54, 1])
is_sorted([1, 2, 6, 2, 'a', 'three'])
is_sorted([1, 2, 'a', 'three'])