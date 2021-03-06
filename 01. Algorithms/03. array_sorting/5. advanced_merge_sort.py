#idea:
  #split array into pieces and for every two pieces, merge them with order, and then merge two pieces each containing 2 numbers and keep merging. 

#code:
def merge_two(list1,list2):
  new_list =[]
  i = 0
  j = 0
  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      new_list.append(list1[i])
      i += 1
    else:
      new_list.append(list2[j])
      j += 1
  while i < len(list1):
    new_list.append(list1[i])
    i += 1
  while j < len(list2):
    new_list.append(list2[j])
    j += 1
  return new_list

def merge_sort(array):
  if len(array) == 0 or len(array) == 1:
    return array
  middle = (len(array)+1)//2 #5//2 = 2
  left = merge_sort(array[:middle])
  right = merge_sort(array[middle:])
  result = merge_two(left,right)
  return result

#complexity:
#time: O(nlogn)
#space: O(n+logn) = O(n)
