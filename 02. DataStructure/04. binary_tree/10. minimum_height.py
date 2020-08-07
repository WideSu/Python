#goal: given a tree, find the minimum height

def get_min_height(root):
  if root is None:
    return 0
  if root.left is None and root.right is None:
    return 0
  left = get_min_height(root.left) if root.left else float('inf')
  right = get_min_height(root.right) if root.right else float('inf')
  return min(left,right) + 1

#complexity:
#time: O(n)
#space: O(height)
