#goal: check whether a binary tree is symmetric.

def check_sym(root):
  if not root:
    return True
  return helper(root.left,root.right)
def helper(root1, root2):
  if not root1 and not root2:
    return True
  if not root1 or not root2:
    return False
  if root1.val != root2.val:
    return False
  return helper(root1.left, root2.right) and helper(root1.right, root2.left)
