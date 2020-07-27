#problem description:
    #given a sorted list, find how many times the target appears and return the times.
    
#example:
    #[1,2,3,3,3,4,6],3 => 3
    
#idea:
    #First, find first occurence and last occurence.
    #Second, last occurence - first occurence + 1 is the goal.
    
#code:
def total_occurence(nums,target):
    occurence = last_occurence(nums,target) - first_occurence(nums,target) + 1
    return occurence

def first_occurence(nums,target):
    if not nums:
        return None
    left = 0 
    right = len(nums) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    return None

def last_occurence(nums,target):
    if not nums:
        return None
    left = 0
    right = len(nums) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] > tagret:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
             left = mid
    if nums[right] == target:
        return right
    elif nums[left] == target:
        return left
    return None

#complexity:
#time complexity: O(logn)
#space complexity: O(1)
