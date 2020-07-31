#pre order: first traverse root then go to its left, until no left node, then traverse right.
def preorder(root):
  res = []
  helper(root,res)
  return res
def helper(root,res):
  if not root:
    return
  res.append(root.val)
  helper(root.left,res)
  helper(root.right,res)
  
#in order: first traverse left node, then root itself and right at last.
def inorder(root):
  res = []
  helper(root,res)
  return res
def helper(root,res):
  if not root:
    return
  helper(root.left,res)
  res.append(root.val)
  helper(root.right,res)
  
#post order: first left node, then right node, and root at last.
def postorder(root):
  res = []
  helper(root,res)
  return res
def helper(root,res):
  if not root:
    return
  helper(root.left,res)
  helper(root.right,res)
  res.append(root.val)
  
#time complexity: O(n)
