#problem description:
    #given a target, find the number which is the target's square root.
    
#example:
    #49 => 7
    
#idea:
    #the square root must be within the range between 1 and target.
    
#code:
def square_root(num):
    if not num:
        return None
    left = 1
    right = num
    while True: #will not stop until 'break' or 'return'
        mid = (left + right) // 2
        if mid**2 > num:
            right = mid - 1
        elif mid**2 < num:
            left = mid + 1
        else:
            return mid
    return None
