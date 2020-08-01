#Q1: print the binary tree in the level order
def level_print(root):
  q = [root] #represent the current level
  next = [] #represent the next level below current
  line = [] #content to print
  while q:
    head = q.pop(0)
    if head.left:
      next.append(head.left)
    if head.right:
      next.append(head.right)
    line.append(head.val)
    if not q:
      print(line)
      if next:
        q = next
        next = []
        line = []
#complexity: time:O(n), space:O(max(len(q)))

#Q2: 
