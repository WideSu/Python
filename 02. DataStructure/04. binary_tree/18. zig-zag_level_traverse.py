def zz_traverse(root):
  if not root:
    return []
  reverse = True
  res = []
  q = [root]
  next = []
  line = []
  while q:
    head = q.pop()
    if head.left:
      next.append(head.left)
    if head.right:
      next.append(head.right)
    line.append(head.val)
    if not q:
      if reverse:
        res.extend(line[::-1]) #append a whole list2 at the end of list1
      else:
        res.extend(line)
      if next:
        q = next
        reverse = not reverse
        next = []
        line = []
  return res
#complexity: time:O(n), space:O(len(q))
