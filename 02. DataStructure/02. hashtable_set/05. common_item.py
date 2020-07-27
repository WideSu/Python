#problem description:
    #Find all numbers that appear in both of the two unsorted arrays, return the common numbers in increasing order.

#idea (using array):
    #traverse one array and then for each item in array 1, check if it is in array 2.
    #write a function to sort the target array or just use sorted(). 
    #sorted(array,reverse = F/T), reverse = False(default) means from small to large, reverse = True means from large to small.

#code:
def common_item_array(array1,array2):
    target = []
    for i in array1:
        if i in array2:
            target.append(i)
    return sorted(target)
    
#idea (using dict):
    #the advantage of using dict is that we can get how many times one item appears in one array, and we can use one key to achieve this since we can use dict.get().
    #so we transfer two array into dict and get the frequency as value
    #we need to find the min value for one key in two dicts.
    
#code:
def common_item_dict(array1,array2):
    countA = {}
    for num in array1:
        countA[num] = countA.get(num,0) + 1
    for num in array2:
        countB[num] = countB.get(num,0) + 1
    common = []
    for num in countA:
        common += [num] * min(countA[num],countB.get(num,0))    #if not common, [num] will * 0 which means common will add null
    return sorted(common)
