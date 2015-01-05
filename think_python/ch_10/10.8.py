def remove_duplicates(x):
    count = 0
    x.sort()
    for i in range(len(x) - 1):
        if  x[i] == x[i + 1]:
            count += 1
    if count > 0:
        print True
    else:
        print False
        
remove_duplicates([1, 2, 3])
remove_duplicates([1, 2, 3, 1, 2, 3])
        