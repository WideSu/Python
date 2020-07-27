#problem description:
    #...

#example:
    #...
    
#idea:
    #basic method has a space complexity which is O(n).
    #we can make a reference and let it points to the current value.
    #make a loop and stop when current value is larger than the one before.

#code:
def advanced_insertion_sort(lst):
    for i in range(1,len(lst)):
        cur_val = lst[i]
        k = i
        while k > 0 and lst[k] < lst[k-1]:
            lst[k] = lst[k-1]
            k -= 1
            lst[k] = cur_val
    return lst

#complexity:
#time complexity: O(n**2)
#space complexity: O(1)
