'''
goal: find smallest k elements from an unsorted array of size n
idea: first heapify the array, and then call pop() k times
'''
import heapq
def kSmallest(array,k):
  if nor array:
    return []
  res = []
  heapq.heapify(array)
  for i in range(min(k,len(array))):
    res.append(heapq.heappop(array))
  return res
  
