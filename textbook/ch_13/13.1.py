import string


def process_file(file):
    hist = dict()
    fin = open(file)
    for line in fin:
        process_line(line, hist)
    return hist
        

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        
        hist[word] = hist.get(word, 0) + 1

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
    
    t.sort(reverse = True)
    return t

x = process_file('text.txt')
y = most_common(x)

def print_most_common(hist, num=10):
    for freq, word in y[0:num]:
        print word, '\t', freq
        
print_most_common(y)