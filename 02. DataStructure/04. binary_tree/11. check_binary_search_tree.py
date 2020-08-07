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
  return res[0]
def inorder(root,prev,res):
  if not root:
    return
  inorder(root.left,prev,res)
  if prev[0] and prev[0] >= root.val:
    res[0] = False
  prev[0] = root.val
  inorder(root.right,prev,res)
#complexity: time: O(n), spcae: O(height)

#solution3:
def check_bst(root):
  return helper(root)[0]
def helper(root):
  if not root:
    return (True, None, None)
  left_res = helper(root.left)
  right_res = helper(root.right)
  if not left_res[0] or not right_res[0]:
    return (False, None, None)
  if left_res[2] amd root.val <= left_res[2]:
    return (False, None, None)
  if right_res[1] and root.val >= right_res[1]:
    return (False, None, None)
  return (True, left_res[1] or root.val, right_res[2] or root.val)
#complexity: time: O(n), spcae: O(height)
