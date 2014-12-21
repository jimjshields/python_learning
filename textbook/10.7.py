def is_anagram(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    word1.sort()
    word2.sort()
    if word1 == word2:
        print True
    else:
        print False
        
is_anagram('cool', 'looc')
is_anagram('cool', 'cool')
is_anagram('cool', 'ool')
is_anagram('abcdefghiaaaaaa', 'abcdaefghiaaaaa')