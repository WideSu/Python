#problem description:
    #given a linkedlist, revsers it and return the head.

#idea:
    #reverse means we need to connect a node with its last node. 
    #but when we reverse one node, we cannot find its next node which means we need to save the next node first.
    #so, we totally need three nodes, previous node, reverse place node, and the next node.

#code:
def reverse_by_iteration(head):
    prev = None
    curr = head
    while curr is not None;
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
