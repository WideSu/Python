#suppose we have a problem that we want to know how many time a word or number appears in a list.

#if we dont know hashtable:

#code:
def frequency(array):
    count_words = []
    count_number = []
    for word in array:
        if word not in count_words:
            count_words.append(word)
            count_number.append(1)
        else:
            for i in range(len(count_words)):
                if word == count_words[i]:
                    count_number[i] += 1
