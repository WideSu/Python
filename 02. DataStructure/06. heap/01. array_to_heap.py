'''
use array as complete binary tree. for each node, its left subtree is (node*2+1) and right subtree is (node*2+2) and its parent node is (node-1)//2.
it is acutually a process that sorts the array.
so, for push and pop operation, we need to re-sort the array
'''

class Heap():
  def __init__(self):
    self.array = []
    
  '''
  push: two processes, first we add value to the array, and second we use binary tree to put the insert value to the righe position.
  '''
  def sift_up(self,array,index): #index represents the current node
    parent_index = (index - 1) // 2
    if parent_index < 0 or array[index] > array[parent_index]: #this is min_heap so if this node is larger than its parent node, no change occurs
      return
    array[index], array[parent_index] = array[parent_index], array[index]
    self.sift_up(array,parent_index)  
  def push(self,value):
    self.array.append(value)
    self.sift_up(self.array,len(self.array) - 1)
  
  '''
  pop: first we get the target node and switch it with the last one, and then put the new head to the right place.
  '''
  def sift_down(self,array,index):
    left = index*2 + 1
    right = index*2 + 2
    small = index
    if left < len(array) and array[left] < array[small]:
      small = left
    if right < len(array) and array[right] < array[small]:
      small = right
    if small != index:
      array[small], array[index] = array[index], array[small]
      self.sift_down(array, small)
  def pop(self):
    res = self.array[0]
    self.array[0], self.array[-1] = self.array[-1], self.array[0]
    self.array.pop() #get rid of the last one
    self.sift_down(self.array, 0)
    return res
