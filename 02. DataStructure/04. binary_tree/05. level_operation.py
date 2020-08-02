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
#complexity: time: O(n), space: O(max(len(q)))

#Q2: given a binary tree where all the right nodes are either leaf nodes or empty, flip it inside down and turn it into a tree where the original right nodes turned into left leaf nodes.
def upside_tree(root):
  if not root:
    return root
  if not root.left and not root.right:
    return root
  new_root = upside_tree(root.left)
  root.left.left = root.right
  root.left.right = root
  root.left = None
  root.right = None
  return new_root
#complexity: time: O(n), space: O(h)
