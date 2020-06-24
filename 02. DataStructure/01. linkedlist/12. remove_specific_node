#problem description:
    #given a linkedlist, we want to remove the node that contains target value

#example:
    #1 -> 10 -> 9 -> 9 -> 8 target=9 => 1->10->8

#idea:
    #we need a prev node to connect linkedlist
    #we also need a curr node to check whether equal to target or not

#code:
def remove_node(head,target):
    if not head:
        return None
    fake_head = ListNode(None)
    fake_head.next = head
    prev = fake_head
    curr = head
    while curr is not None:
        if curr.value == target:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = prev.next
            curr = curr.next
    return fake_head.next
            
