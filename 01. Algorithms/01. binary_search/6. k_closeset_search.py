#problem description:
    #given a sorted list, find k numbers that are close to target and return the k list.
    
#example:
    #[1,3,4,5,6,10],7,3 => [6,5,10]
    
#idea:
    #First, find the closest number and find its index.
    #Second, define a targetlist and append the closest number.
    #Third, get the left and right that is near closest number.
    #Fourth, write a loop which runs when len(targetlist) < k and (left >= 0 or right <= total).
    #Finally, return the targetlist
    
#code:
def k_closest_search(nums,target,k):
    if not nums:
        return None
    left = 0
    right = len(nums) - 1
    closest = None
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid
        else:
            closest = mid
            break
    if closest != None:
        if abs(nums[left]-target) < abs(nums[right]-target):
            closest = left
        elif abs(nums[left]-target) > abs(nums[right]-target):
            closest = right
    targetlist = []
    if k == 0:
        return targetlist
    targetlist.append(nums[closest])
    left = closest - 1
    right = closest + 1
    total = len(nums) - 1
    while len(targetlist) < k and (left >= 0 or right <= total):
        if right <= total and (left < 0 or abs(nums[right]-target) < abs(nums[left]-target)):
            targetlist.append(nums[right])
            right += 1
        elif left >= 0 and (right > total or abs(nums[right]-target) > abs(nums[left]-target)):
            targetlist.append(nums[left])
            left -= 1
    return targetlist
