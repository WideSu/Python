#goal: turn left node to right for each node in binary tree.

def invert(root):
  if not root:
    return root
  tmp = root.right
  root.right = invert(root.left)
  root.left = invert(tmp)
  return root
