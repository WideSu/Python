#problem description:
    #merge two linkedlist into one or split one linkedlist in half.

#code:
def merge(head1,head2):
    fake_head = ListNode(None)
    curr = fake_head
    while head1 is not None and head2 is not None:
        if head1.value < head2.value:
            curr.next = head1
            head1 = head1.next 
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    if head1 is not None:
        curr.next = head1  #because the rest of the linkedlist is linked originally so that we just connect the tail with the head. so we can only use for loop not while loop since head will be alwasy not None.
    elif head2 is not None:
        curr.next = head2
    return fake_head.next
    

def split_linkedlist(head):
    slow_move = head
    fast_move = head.next
    while fast_move is not None and fast_move.next is not None:
        slow_move = slow_move.next
        fast_move = fast_move.next.next  #this means the fast_move node is moving twice fast as slow_move so that when it equal to tail, the slow_move node is at half
    cut_node = slow_move.next
    slow_move.next = None  #cut first half and second half's connection
    head1 = head
    head2 = cut_node
    return head1, head2
