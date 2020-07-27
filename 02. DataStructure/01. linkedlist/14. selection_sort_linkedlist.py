def selectionSort(self, head):
  new_head = ListNode(None)
  new_head.next = head
  helper = new_head
  while helper.next:
    prev, curr = helper, helper.next
    min_node, min_node_prev = curr, prev
    while curr:
      if curr.val < min_node.val:
        min_node, min_node_prev = curr, prev
      prev, curr = curr, curr.next
    min_node_prev.next = min_node.next
    next_node = helper.next
    helper.next = min_node
    min_node.next = next_node
    helper = helper.next
  return new_head.next
