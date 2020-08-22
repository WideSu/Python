def find_max(root):
  if not root:
    return None
  return find_max(root.right) or root
def find_max_small(root,target):
  if not root:
    return None
  if root.key == target:
    return find_max(root.left)
  elif root.key > target:
    return find_max_small(root.left,target)
  else:
    return find_max_small(root.right,target) or root
