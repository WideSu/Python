#goal: find the lowest common ancestor for two node, ones ancestor can be itself.

def lowest_common_ancestor(root,p,q):
  if root is None:
    return None
  elif root == p or root == q:
    return root
  lres = lowest_common_ancestor(root.left,p,q)
  rres = lowest_common_ancestor(root.right,p,q)
  if lres and rres:
    return root
  if lres:
    return lres
  return rres
