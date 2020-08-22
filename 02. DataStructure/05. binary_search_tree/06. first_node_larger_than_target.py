#goal: given a bst, find the first node containing a value that is larger than our target value,

'''
idea:
  if the value equal to target, the node we need will be the left most node of the right subtree.
  if value is smaller than the target, then the answer node is contained inside the right subtree.
  if value is larget than the target, then the answer node is either contianed inside the left subtree or the root value itself.
'''

def find_first_larger(root,target):
  if not root:
    return None
  if root.key == target:
    return find_min(root.right)
  elif root.key < target:
    return find_first_larger(root.right, target)
  else:
    return find_first_larger(root.left, target) or root
def find_min(root):
  if not root:
    return None
  return find_min(root.left) or root
