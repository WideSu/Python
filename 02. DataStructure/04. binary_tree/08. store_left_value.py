#goal: for each node in tree, store the number of nodes in its left child subtree.
class TreeNode():
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None
    self.total_left = 0
def total_subtree(node):
  if node is None:
    return 0
  left_total = total_subtree(node.left)
  right_total = total_subtree(node.right)
  node.total_left = left_total
  return 1 + left_total + right_total
