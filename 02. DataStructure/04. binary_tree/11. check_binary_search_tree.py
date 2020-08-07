/..g#1bnary search tree: for every single node in the tree, the values in its left subtree are all smaller than its value, and the value in its right subtree are all larger than its value.

#solution1:
def bst(root):
  if root is None:
    return True
  min_val = float('-inf')
  max_val = float('inf')
  return check_bst(root,min_val,max_val)
def check_bst(root,min_val,max_val):
  if root is None:
    return True
  if root.val <= min_val or root.val >= max_val:
    return False
  return check_bst(root.left,min_val,root.val) and check_bst(root.right,root.val,max_val)

#complexity: time: O(n), space: O(height)

#solution2:
def check(root):
  prev = [None]
  res = [True]
  inorder(root,prev,res)
  
