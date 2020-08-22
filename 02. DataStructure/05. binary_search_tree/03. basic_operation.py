class Node():
  def __init__(self,key,value):
    self.key = key
    self.value = value
    self.left = self.right = None

#search:
#recursive solution:
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

#insert value:
#recursive:
class BST():
  def __init__(self):
    self.root = None
  def _insert(self,root,key,value):
    if not root:
      return Node(key,value)
    if key < root.key:
      root.left = self._insert(root.left,key,value)
    elif key > root.key:
      root.right = self._insert(root.right,key,value)
    else:
      root.value = value
    return root
  def insert(self,key,value):
    self.root = self._insert(self.root,key,value)
#iterative:
class BST():
  def __init__(self):
    self.root = None
  def insert(self,key,value):
    if not self.root:
      self.root = Node(key,value)
      return
    curr,prev,is_left = self.root,None,None
    while curr:
      prev = curr
      if key < curr.key:
        is_left = True
        curr = curr.left
      elif key > curr.key:
        is_left = False
        curr = curr.right
      else:
        curr.value = value
        break
    if not curr:
      node = Node(key,value)
      if is_left:
        prev.left = node
      else:
        prev.right = node

#delete value:
class BST():
  def __init__(self):
    self.root = None
  #delete min value
  def delete_min(self,root):
    if not root.left:
      return root.right
    root.left = self.delete_min(root.left)
    return root
  #delete
  def delete(self,root,key):
    if not root:
      return None
    if key < root.key:
      root.left = self.delete(root.left,key)
    elif key > root.key:
      root.right = self.delete(root.right,key)
    else:
      if not root.right:
        return root.left
      if not root.left:
        return root.right
      t = root
      root = self.min(t.right)
      root.right = self.delete_min(t.right)
      root.left = t.left
    return root
