def remove_duplicates(x):
    x.sort()
    for i in range(len(x) - 2):
        if  x[i] == x[i + 1]:
            del x[i + 1]
    print x
        
remove_duplicates([1, 2, 3])
remove_duplicates([1, 2, 3, 1, 2, 3])
        