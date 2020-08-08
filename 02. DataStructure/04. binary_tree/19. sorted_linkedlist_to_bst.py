class TreeNode():
  def __init__(self,value):
    self.left = None
    self.right = None
    self.val = value
def to_bst(head):
  arr = []
  while head:
    arr.append(head.val)
    head = head.next
  return creat_bst(arr)
def creat_bst(arr):
  if not arr:
    return None
  return bst(arr,0,len(arr)-1)
def bst(arr,start,end):
  if start > end:
    return None
  mid = (start + end) // 2
  root = TreeNode(arr[mid])
  root.left = bst(arr,start,mid-1)
  root.right = bst(arr,mid+1, end)
  return root
#complexity: time:O(n) space:O(n)
