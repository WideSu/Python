#goal: Design your implementation of the circular queue. 
##The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer"
class Solution(object):
    def __init__(self, k): #Initialize your data structure here. Set the size of the queue to be k.
        self.items = [None] * (k+1)
        self.head = self.tail = 0

    def enQueue(self, value): #Insert an element into the circular queue. Return true if the operation is successful.
        if self.isFull():
          return False
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % len(self.items)
        return True
        

    def deQueue(self): #Delete an element from the circular queue. Return true if the operation is successful.
        if self.isEmpty():
          return False
        self.head = (self.head + 1) % len(self.items)
        return True
        

    def Front(self): #Get the front item from the queue.
        if self.isEmpty():
          return -1
        else:
          return self.items[self.head]
        

    def Rear(self): #Get the last item from the queue.
        if self.isEmpty():
          return -1
        else:
          return self.items[(self.tail - 1 + len(self.items)) % len(self.items)]
        

    def isEmpty(self): #Checks whether the circular queue is empty or not.
        return self.head == self.tail
        

    def isFull(self): #Checks whether the circular queue is full or not.
        return (self.tail - self.head + len(self.items)) % len(self.items) == len(self.items) - 1
