#solution1:
def check_helper(root,prev):
  if not root:
    return True
  if not check_helper(root.left,prev):
    return False
  if prev[0] >= root.val:
    return False
  prev[0] = root.val
  return check_helper(root.right,prev)
def check(root):
  prev = [None]
  return check_helper(root,prev)

#solution2:
def check_helper(root):
  if not root:
    return True, None, None
  lr,lmin,lmax = check_helper(root.left)
  rr,rmin,rmax = check_helper(root.right)
  return lr and rr and (lmax is None or lmax < root.val) and (rmin is None or root.val < rmin), lmin if lmin is not None else root.val, rmax if rmax is not None else root.val
def check(root):
  return check_helper(root)[0]
