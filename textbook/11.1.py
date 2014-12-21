fin = open('words.txt')

words_dict = dict()

i = 0

for line in fin:
    word = line.strip()
    words_dict[word] = i
    i += 1
    
print words_dict