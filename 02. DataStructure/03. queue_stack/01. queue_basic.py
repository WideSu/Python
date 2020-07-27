#idea: queue is a datastructure that all elements follow first-in-first-out policy.

#what the code should achieve: add element to the queue, remove element in the queue, check if queue is empty, find the next removed element

#code:
class queue(object):
  def __init__(self):
    self.items = []
  def __len__(self):
    return len(self.items)
  def enqueue(self,item):
    self.items.append(item)
  def dequeue(self):
    if self.empty():
      return None
    item = self.items[0]
    del self.items[0]
    return item
  def empty(self):
    return len(self.items) == 0
  def front(self):
    if self.empty():
      return None
    return self.items[0]

#time complexity: O(1)

#example:
q = queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(11)
print(q.empty())
  #->False
print(q.front())
  #->5
print(q.dequeue())
  #->5
