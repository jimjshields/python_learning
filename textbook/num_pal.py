def num_check(num):

    num = str(num)
    i = 0
    j = 5
    
    for n in num:
        if num[i] != num [j]:
            return False
        
        i += 1
        j -= 1

    print num

def num_pal():
    i  = 100000
    while i < 1000000:
        num_check(i)
        i += 1

num_pal()    


