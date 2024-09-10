def single_root_words(root_word, *other_words):
    same_words = []
    words_low = ''
    root_word_low = root_word.lower()
    for words in other_words:
        words_low = words.lower()
        if words.find(root_word,0) != -1:
            same_words.append(words)
        if root_word_low.find(words_low, 0) != -1:
            same_words.append(words)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)