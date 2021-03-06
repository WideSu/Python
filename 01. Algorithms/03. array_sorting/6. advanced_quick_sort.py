def quick_sort(array):
  quick_sort(array,0,len(array)-1)
  return array
  
def partition(lst,left,right):
  start = left
  end = right - 1
  import random
  rand = random.randint(left,right)
  lst[rand], lst[right] = lst[right], lst[rand]
  pivot = lst[right]
  while start <= end:
    if lst[start] < pivot:
      start += 1
    elif lst[end] >= pivot:
      end -= 1
    else:
      lst[start],lst[end] = lst[end],lst[start]
      start += 1
      end -= 1
  lst[start], lst[right] = lst[right], lst[start]
  return start

def quick_sort_recursion(lst,left,right):
  if left >= right:
    return 
  pivot = self.partition(lst,left,right)
  quick_sort_recursion(lst,left,pivot-1)
  quick_sort_recursion(lst,pivot+1,right)
