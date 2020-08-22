#idea: empty tree will return None, if it is not empty, then just find the left subtree because for bst, left is always the smallest one comparing with root and right sub.
def find_min(root):
  if not root:
    return None
  return find_min(root.left) or root
