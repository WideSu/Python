#problem decription: 
       #a sorted (ordered, like 1,2,3,4,5) list, find the number that is equal to target, and return its index.
       
#example: 
       #[1,2,3,4,5],5 => index=4
       
#idea: 
       #First, find the left (index) and right (index) of the list. 
       #Second, use left and right to get mid index. 
       #Third, find whether list[mid] == target. 
       #Finally, use left = mid + 1 and right = mid - 1 to run the loop.
       
#code:
def classical_binary_search(nums,target):
    if not nums:
        return None
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target：
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return None
    
#complexity:
time complexity: O(logn)
space complexity: O(1)
       
