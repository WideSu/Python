#goal: sort a array that contains only -1, 0, 1.

#code:
def rainbow_sort(array):
  left = 0
  right = len(array) - 1
  index = 0
  while index <= right:
    if array[index] == -1:
      array[index], array[left] = array[left], array[index]
      left += 1
      index += 1
    elif array[index] == 1:
      array[index], array[right] = array[right], array[index]
      right -= 1
    else:
      index += 1
  return array
