'''
goal: find smallest k elements from an unsorted array of size n
idea: first heapify the array, and then call pop() k times
'''

#min heap case:
import heapq
def k_smallest(array,k):
  if nor array:
    return []
  res = []
  heapq.heapify(array)
  for i in range(min(k,len(array))):
    res.append(heapq.heappop(array))
  return res
  
#max heap case:
def k_smallest(array,k):
  if not array:
    return array
  if k >= len(array):
    return array
  res = [-elem for elem in array[0:k]]
  heapq.heapify(res)
  for i in range(k,len(array)):
    if array[i] < -res[0]:
      heapq.heappop(res)
      heapq.heappush(res,-array[i])
  return [-elem for elem in res]
