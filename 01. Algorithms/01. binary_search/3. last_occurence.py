#problem description:
    #given a sorted list, find where the target last occurs. return its index
    
#example:
    #[1,3,3,4,6],3 => index = 2
    
#idea:
    #First, find left and right.
    #Second, set while loop and get mid.
    #Third, compare list[mid] with target, but do not return mid once they are equal.
    #Finally, discuss which index should be accepted.
    
#code:
def last_occurence(nums,target):
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
            left = mid
    if nums[right] == target:
        return right
    elif nums[left] == target:
        return left
    else:
        return None

#complexity:
#time complexity: O(logn)
#space complexity: O(1)
