#problem description:
    #given a sorted dictionary but the size is unknown, find the number and return its index.
    
#example:
    #[1,2,3,4,...],3 => index = 2
    
#idea:
    #dic.get(index) will return the index's value and None if out of index.
    #use dic.get() to expand the search area until the target number is included.
    
#code:
def unknownsize_search(dic,target):
    if not dic:
        return None
    start = 1
    while dic.get(start) is not None and dic.get(start) < target:
        start = start * 2
    left = 0 
    right = start
    while left <= right:
        mid=(left + right) // 2
        if dic.get(mid) = None:
            right = mid - 1
        elif dic.get(mid) > target:
            right = mid - 1
        elif dic.get(mid) < target:
            left = mid + 1
        else:
            return mid
    return None
    
