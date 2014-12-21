def age_check():
    i = 0
    j = 36
    
    while j <= 110:
        i = str(i)
        i_len = len(i)
        j = str(j)
        j_len = len(j)
        for n in i:
            if i_len != j_len:
                return False
            if i[n] != j[-n]:
                return False
            n += 1
        return True
        print i,
        print j
        i = int(i)
        j = int(j)
        j += 1
            

age_check()