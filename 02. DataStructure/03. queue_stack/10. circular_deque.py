#goal: Design implementation of the circular double-ended queue (deque).
class CircularQueue(object):
    def __init__(self, k):
      self.size = 0
      self.items = [None] * (k + 1) #for example, k=2 -> [None,None,None]
      self.first = 0 #first will point to the position where we will insert the new front element of this queue
      self.last = 1 #last will point to the position where we will insert the new rear element of this queue
      
    def insertFront(self, value): #Adds an item at the front of Deque. Return true if the operation is successful
      if self.isFull():
        return False
      self.items[self.first] = value
      self.first = (self.first - 1 + len(self.items)) % len(self.items)
      self.size += 1
      return True

    def insertLast(self, value): #Adds an item at the rear of Deque. Return true if the operation is successful.
      if self.isFull():
        return False
      self.items[self.last] = value
      self.last = (self.last + 1) % len(self.items)
      self.size += 1
      return True

    def deleteFront(self): #Deletes an item from the front of Deque. Return true if the operation is successful.
      if self.isEmpty():
        return False
      self.first = (self.first + 1) % len(self.items)
      self.size -= 1
      return True

    def deleteLast(self): #Deletes an item from the rear of Deque. Return true if the operation is successful.
      if sel.isEmpty():
        return False
      self.last = (self.last - 1 + len(self.items)) % len(self.items)
      self.size -= 1
      return True

    def getFront(self): #Get the front item from the deque.
      if self.isEmpty():
        return -1
      else:
        return self.items[(self.first + 1) % len(self.items)]

    def getRear(self): #Get the last item from the deque.
      if self.isEmpty():
        return -1
      else:
        return self.items[(self.last - 1 + len(self.items)) % len(self.items)]

    def isEmpty(self): #Checks whether the circular deque is empty or not.
      return self.size == 0

    def isFull(self): #Checks whether the circular deque is full or not.
      return self.size == len(self.items) - 1
