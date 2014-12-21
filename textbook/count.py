def count(word, letter, start):
    index = start
    count = 0
    while index < len(word):
        if word[index] == letter:
            count +=1
        index += 1
    print count
    
count('banana', 'a', 2)
count('cool cool cool cool beans', 'o', 2)