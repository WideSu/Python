#problem description:
    #gievn a sorted list, find the number that is the closest to target (if no target number exists), and return its index.
    
#example:
    #[1,2,4,5,9],8 => index = 4
    
#idea:
    #First, find left and right
    #Second, set while left < right - 1 loop.
    #Third, cannot give up any number since it may be the closest one.
    #Finally, compare left and right and their distance with target.
    
#code:
def closest_number_search(nums,target):
    if not nums:
        return None
    left = 0
    right = len(nums) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid
        else:
            return mid
    if abs(nums[left]-target) < abs(nums[right]-target):
        return left
    elif abs(nums[left]-target) > abs(nums[right]-target):
        return right

#complexity:
#time complexity: O(logn)
#space complexity: O(1)
