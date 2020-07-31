def get_height(root):
  if not root:
    return 0
  left = get_height(root.left)
  right = get_height(root.right)
  return 1 + max(left,right)
