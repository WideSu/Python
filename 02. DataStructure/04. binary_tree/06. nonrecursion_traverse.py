def preorder(root):
  output = []
  if not root:
    return output
  stack = [(root, 1)]
  while stack:
    node, count = stack.pop()
    if count == 1:
      output.append(node.val)
      stack.append((node, count+1))
      if node.left:
        stack.append((node.left, 1))
    if count == 2:
      if node.right:
        stack.append((node.right, 1))
  return output

def inorder(root):
  output = []
  if not root:
    return output
  stack = [(root,1)]
  while stack:
    node, count = stack.pop()
    if count == 1:
      stack.append((node, count+1))
      if node.left:
        stack.append((node.left,1))
    if count == 2:
      output.append(node.val)
      if node.right:
        stack.append((node.right,1))
  return output

def postorder(root):
  output = []
  if not root:
    return root
  stack = [(root,1)]
  while stack:
    node, count = stack.pop()
    if count == 1:
      stack.append((node,count+1))
      if node.left:
        stack.append((node.left,1))
    if count == 2:
      stack.append((node,count+1))
      if node.right:
        stack.append((node.right,1))
    if count == 3:
      output.append(node.val)
  return output
