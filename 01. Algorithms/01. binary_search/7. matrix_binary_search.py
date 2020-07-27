#problem description:
    #given a matrix and the numbers within it are sorted, find the target number and return its matrix index.
    
#example:
    #matrix = ([0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]),12 => [3,0]
    
#idea:
    #think matrix as a one dimensional list, the index of one number equal rowposition * colnumber + colposition
    
#code:
def matrix_binary_search(matrix,target):
    if not matrix:
        return None
    row = len(matrix)
    col = len(matrix[0])
    left = 0
    right = row * col - 1
    while left <= right:
        mid = (left + right) // 2
        midrow = mid // col
        midcol = mid % col
        if matrix[midrow][midcol] < target:
            left = mid + 1
        elif matrix[midrow][midcol] > target:
            right = mid - 1
        else:
            return midrow, midcol
    return None
