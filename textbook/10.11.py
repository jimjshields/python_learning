def find_word(x, word):
    x.sort()
    if word < x[(len(x)/2)]:
        if word in x[:len(x)/2]:
            print True
    elif word in x[len(x)/2:]:
        print True
    else:
        print False

find_word(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'], 'c')
find_word(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'], 'a')
find_word(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'], 'q')
find_word(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'], 'g')