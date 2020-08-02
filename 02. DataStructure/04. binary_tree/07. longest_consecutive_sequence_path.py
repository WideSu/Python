#given a binary tree, find the length of the longest consecutive sequence path.
def consecutive(curr,parent,currlen):
  if not curr:
    return currlen
  size = 1
  if parent and curr.val == parent.val + 1:
    size = currlen + 1
  return max(currlen, consecutive(curr.left,curr,size), consecutive(curr.right,curr,size))
