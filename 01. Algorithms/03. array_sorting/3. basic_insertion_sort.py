#problem description:
    #...

#example:
    #...

#idea: 
    #create a new list and append data with order.
    #how to add the data orderly is the key.

#code:
def basic_insertion_sort(lst):
    new_array = []
    for i in range(len(array)):                               #traverse all elements and append to new array
        idx = len(new_array) - 1                              #the one before new added element
        new_array.append(array[i])
        while idx >= 0:                                       
            if new_array[idx] > new_array[idx + 1]:           #compare new added data with other already existed data
                new_array[idx],new_array[idx+1] = new_array[idx+1],new_array[idx]
            else:
                break
            idx -= 1
    return new_array

#complexity:
#time complexity: O(n**2)
#space complexity: O(n)
