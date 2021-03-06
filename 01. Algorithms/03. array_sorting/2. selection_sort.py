#problem description:
    #...

#example:
    #...
    
#idea:
    #find the largest(or smallest) for each round and put it to the tail.
    #we also need a method to find the max(or min).

#code:
def find_max(lst):
    max_index = 0
    for i in range(len(lst)):
        if lst[i] > lst[max_index]:
            max_index = i
    return max_index

def slection_sort(lst):
    for i in range(len(lst)-1,0,-1): #i represents the tail for each round
        max_index = 0
        for j in range(i+1):
            if lst[j] > lst[max_index]:
                max_index = j
        lst[i],lst[max_index] = lst[max_index],lst[i]
    return lst

#complexity:
#time complexity: O(n**2)
#space complexity: O(1)
