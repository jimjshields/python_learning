def has_duplicates(d):
    temp = {}
    for i in d:
        if i in temp:
            print True
        temp[i] = i
    print temp
        
my_dict = {1: 'cool', 2: 'not cool', 1: 'cool beans'}

has_duplicates(my_dict)