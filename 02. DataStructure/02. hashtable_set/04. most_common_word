def most_common_word(array):
    count = {}
    for word in array:
        if word in count:
            count[word] += 1        #if in dict, it means the key already exists and has the value at least 1
        else:
            count[word] = 1        
    best = max(count.values())      #count.values() return a list of value to each key, use max to find the max value
    word_list = []
    for word, count in count.items():
        if count == best:
            word_list.append(word)
    return word_list
