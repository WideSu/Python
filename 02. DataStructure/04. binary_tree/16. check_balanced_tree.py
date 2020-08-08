#goal: check whether a tree is balanced (the depths of every node's left and right subtree deffer by at most 1).

def check_bal(root):
  if not root:
    return True
  left = get_height(root.left)
  right = get_height(root.right)
  if abs(left - right) > 1:
    return False
  return check_bal(root.left) and check_bal(root.right)
def get_height(root):
  if not root:
    return 0
  left = get_height(root.left)
  right = get_height(root.right)
  return 1 + max(left,right)
