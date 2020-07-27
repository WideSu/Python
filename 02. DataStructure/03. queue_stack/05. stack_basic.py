#stack -> last in first out. 

#code:
class Stack(object):
  def __init__(self):
    self.items = []
    self.min = []
  def __len__(self):
    return len(self.items)
  def empty(self):
    return len(self.items) == 0
  def push(self,value):
    self.items.append(value)
    if not self.mins or self.mins[-1] >= value:
      self.mins.append(value)
  def pop(self):
    if self.empty():
      return None
    item = self.items.pop()
    if item == self.mins[-1]:
      self.mins.pop()
    return item
  def top(self): #top is the next value pop out
    if self.empty():
      return None
    return self.items[-1]
  def min(self):
    if self.mins:
      return self.mins[-1]
    else:
      return -1

#time complexity: O(1)
