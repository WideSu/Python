#problem decription:
    #given a sorted list, and a target, find where the target first occurs and return its index.
    
#example:
    #[1,2,3,3,4,6],3 => index = 2
    
#idea:
    #First,find left and right.
    #Second,use left and right to get mid.
    #Third, same condition with classical binary search, but when list[mid] == target, should let right = mid.
    #Finally, we get two near number and discuss which one is first
    
#difference with classical binary search:
    #if we find the target, we cannot return it because what we want is where it first occurs. so we have right = mid.
    #because of right = mid, we cannot use while left <= right anymore because it will not stop if left and right both equal target.
    
#code:
def first_occur(nums,target):
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
    else:
        return None

#complexity:
#time complexity: O(logn)
#space complexity: O(1)
