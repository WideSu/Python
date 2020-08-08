#goal: given a binary tree, determine if the tree has a root-to-leaf path such that adding up all values to equal target.

def check(root,target):
  return sum_path(root,0,target)
def sum_path(curr,partial,target):
  if curr is None:
    return False
  partial += curr.val
  if curr.left is None and curr.right is None:
    return partial == target
  return sum_path(curr.left,partial,target) or sum_path(curr.right,partial,target)
