def three_consecutive(word):
    i = 0
    
    if len(word) < 6:
        print False
        
    while i < len(word) - 4:
        if word[i] == word[i + 1]:
            if word[i + 2] == word[i + 3]:
                if word[i + 4] == word[i + 5]:
                    print True
        i += 1
print False
            
three_consecutive('cool')
three_consecutive('bookkeeper')
three_consecutive('cool beans')