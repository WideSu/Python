#goal: given a stream of integers and a window size, calculated the moving average of all integers in the sliding window.

#idea: add element to the queue first, and use a parameter to calculate sum of queue. then check the size and remove number out of size.

#code:
from collections import deque
class MovingAverage(object):
  def __init__(self,size):
    self.dq = deque()
    self.max_size = size
    self.sum = 0
  def next(self,value):
    self.dq.append(value)
    self.sum += value
    if len(self.dq) > self.max_size:
      self.sum -= self.dq.popleft() #popleft will remove and return the removed value
    return self.sum / len(self.dq)

#example:
s = MovingAverage(2)
print(s.next(1))
  #->1.0
print(s.next(5))
  #->3.0
print(s.next(6))
  #->5.5
