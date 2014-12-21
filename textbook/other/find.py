def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            print index
            return index
        index += 1
    print -1
    return -1

find ('Hello, world!', 'o', 5)