def mergeSort(head):
  if not head or not head.next:
    return head
  one, two = split(head)
  one = mergeSort(one)
  two = mergeSort(two)
  return merge(one,two)
  
def split(head):
  slow, fast = head, head.next
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  head2 = slow.next
  slow.next = None
  return head, head2
  
def merge(one,two):
  prev = ListNode(None)
  curr = prev
  while one and two:
    if one.val < two.val:
      curr.next = one
      one = one.next
      curr = curr.next
    else:
      curr.next = two
      two = two.next
      curr = curr.next
  if one: 
    curr.next = one
  else:
    curr.next = two
  return prev.next 
