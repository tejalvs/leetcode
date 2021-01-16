def wordFrequency(sample):
    wordlist={}
    print(sample)
    for word in sample:
        if word in wordlist.keys():
            wordlist[word]+=1
        else:
            wordlist[word] = 1
    return wordlist




def Main():
    doc = [ "Given", "a", "document", "represented", "as", "a", "list", "of", "words", "write",
             "a", "function", "that", "prints", "each", "word", "and", "its", "number", "of",
             "occurrences", "in", "the", "order", "of", "descending", "frequency"]
    word_frequency=wordFrequency(doc)
    word_frequency_sorted=sorted(word_frequency.items(), key=lambda x:x[1],reverse=True)
    print(word_frequency_sorted)
Main()