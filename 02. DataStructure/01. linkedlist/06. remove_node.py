#problem description:
    #given a linkedlist, remove the value according to its index.
    
#idea:
    #almost same as adding.
    #but when we get the prev_node, we need to make sure that prev_node and its next is not None otherwise we dont need to remove anything.

#code:
def remove_by_index(head,index):
    if not head:
        return None
    fake_head = ListNode(None)
    fake_head.next = head
    prev_node = search_by_index(fake_head,index)
    remove_node = prev_node.next
    prev_node.next = remove_node.next
    remove_node.next = None
    return fake_head.next
