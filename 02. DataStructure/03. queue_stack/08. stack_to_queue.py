#use two stacks to achieve queue
class Queue:
  def __init__(self):
    self.s1 = []
    self.s2 = []
    self.head = None
  def enqueue(self,x):
    if not self.s1:
      self.head = x
    self.s1.append(x)
  def dequeue(self):
    if not self.s2:
      while self.s1:
        self.s2.append(self.s1.pop())
    retturn self.s2.pop()
  def is_empty(self):
    return not self.s1 and not self.s2
  def peek(self):
    if self.s2:
      reyirm self.s2[-1]
    return self.head
  def size(self):
    return len(self.s1) + len(self.s2)
