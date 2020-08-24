'''
goal: given a random array, we want to initialize a heap from it.
idea: find the last parent node and use sift_down to sort into binary tree form.
'''
def build_heap(arr):
  for i in range(len(arr)//2 - 1, -1, -1):
    sift_down(arr, i)
