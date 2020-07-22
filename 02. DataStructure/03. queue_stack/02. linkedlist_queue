class ListNode(object):
  def __init__(self,number):
    self.val = number
    self.next = None
class queue(object):
  def __init__(self):
    self.size = 0
    self.head, self.tail = None, None
  def __len__(self):
    return self.size
  def empty(self):
    return self.size == 0
  def enqueue(self,value):
    if not self.empty():
      self.tail.next = ListNode(value)
      self.tail = self.tail.next
    else:
      self.head = self.tail = ListNode(value)
    self.size += 1
  def dequeue(self):
    if self.empty():
      return None
    value = self.head.val
    self.head = self.head.next
    if not self.head:
      self.tail = None
    self.size -= 1
    return value
  def front(self):
    if self.empty():
      return None
    return self.head.value

