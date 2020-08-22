#goal: given a key, find its corresponding value

#recursive solution:
class Node():
  def __init__(self,key,value):
    self.key = key
    self.value = value
    self.left = self.right = None
class BSTNode():
  def __init__(self):
    self.root = None
  def _query(self,root,key):
    if not root:
      return None
    if key < root.key:
      return self.query(root.left,key)
    if key > root.key:
      return self.query(root.right,key)
    else:
      return root.value
  def query(self,key):
    return self._query(self.root,key)

#iterative solution:
class BST():
  def __init__(self):
    self.root = None
  def query(self,key):
    if not self.root:
      return None
    curr = self.root
    while curr:
      if key < curr.key:
        curr = curr.left
      elif key > curr.key:
        curr = curr.right
      else:
        return curr.value
    return None
