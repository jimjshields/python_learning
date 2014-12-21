def inverse_dict(d):
    inverse = dict()
    for k in d:
        val = d[k]
        setdefault(val, k)
    print inverse
        
my_dict = {1: 'cool', 2: 'not cool', 3: 'cool beans'}

inverse_dict(my_dict)