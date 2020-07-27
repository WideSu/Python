#problem description:
    #we know that there is a max number that a computer can work with, so we can use linkedlist two deal with this.
    #suppose we have two linkdelists and each node contains one interger (less than 10), we want to add node's value in same postition and return the added linkedlist

#example:
    #1->2->3 and 3->4->5 => 4->6->8 => 8->6->4 => 864

#idea:
    #we need to reverse first because we need to calculate first at the first digit
    #we alse need to think the situation that two number's sum bigger than 10
    #at last, we need to deal with the problem that two number with different length

#code:
def reverse_linkedlist(head):
    prev = ListNode(None)
    curr = head
    while curr is not None:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    return prev

def add_list(head1,head2):
    new_head1 = reverse_linkedlist(head1)
    new_head2 = reverse_linkedlist(head2)
    fake_head = ListNode(None)
    curr = fake_head
    carry = 0
    while new_head1 and new_head2:
        temp_sum = new_head1.value + new_head2.value + carry
        new_number = temp_sum % 10
        carry = temp_sum // 10
        new_digit = ListNode(new_number)
        curr.next = new_digit
        curr = curr.next
        new_head1 = new_head1.next
        new_head2 = new_head2.next
    while new_head1:
        temp_sum = new_head1.value + carry
        new_number = temp_sum % 10
        carry = temp_sum // 10
        new_digit = ListNode(new_number)
        curr.next = new_digit
        curr = curr.next
        new_head1 = new_head1.next
    while new_head2:
        temp_sum = new_head2.value + carry
        new_number = temp_sum % 10
        carry = temp_sum // 10
        new_digit = ListNode(new_number)
        curr.next = new_digit
        curr = curr.next
        new_head2 = new_head2.next
    if carry > 0:
        curr.next = ListNode(carry)
    return reverse_linkedlist(fake_head.next)
