class Stack:
  def __init__(self):
    self.stack = []
  def is_empty(self):
    return len(self.stack) == 0
  def max(self):
    if not self.is_empty()：
      return self.stack[-1][1]
    raise Exception('max():empty stack')
  def push(self,x):
    tmp = x
    if not self.is_empty():
      tmp = max(tmp,self.max())
    self.stack.append((x,tmp))
  def pop(self):
    if self.is_empty():
      raise Exception('pop(): empty stack')
    elem = self.stack.pop()
    return elem[0]
