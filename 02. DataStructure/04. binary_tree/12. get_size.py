def get_size(root):
  if not root:
    return 0
  left = get_size(root.left)
  right = get_size(root.right)
  return 1 + left + right
