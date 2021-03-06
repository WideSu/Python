#code:
def reverse_by_recursion(head):
    if not head or not head.next:
        return head
    new_head = reverse_by_recursion(head.next)
    head.next.next = head
    head.next = None
    return new_head

#explanation in detail:
'''
suppose we have 4 nodes in a linkedlist
1. new_head = reverse_by_recursion(head.next) will return the tail beacuse its next == None
2. because when returning the tail, the function stops so for node 4, the code after reverse_by_recursion will not run
3. after new_head = node4, it returns to head = node3
4. node3.next is node4, node4.next = head means node4 points to node3
5. node3.next = None means we disconnect node3 with node4
6. at last, it return the new_head which is node4 in this case to its last loop
7. so when head = node2, new_head is still new_head (node4)
8. actually, new_head does not effect the process because what we use is head, head.next and head.next.next and the new
_head here is just used to record the new_head because we need to know the head to know the whole linkedlist
'''
