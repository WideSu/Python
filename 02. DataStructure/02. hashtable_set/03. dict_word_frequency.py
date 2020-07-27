#use dictionary to deal with word frequency problem

#code:
#with list:
def count_word(arrary):
    count_word = []
    count_number = []
    for word in array:
        if word not in count_word:
            count_word.append(word)
            count_number.append(1)
        else:
            for i in range(len(count_word)):
                if word == count_word[i]:
                    count_number += 1
    return count_number,count_word

#with dict:
def count_word(array):
    freq = {}
    for word in array:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
