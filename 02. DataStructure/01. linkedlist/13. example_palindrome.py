#problem description:
    #given a linkedlist, we want to check whether it is palindrome or not.

#example:
    #a -> b -> c -> b -> a => return true

#idea:
    #we first copy the linkedlist
    #and then reverse the new linkedlist
    #we campare these two linkedlist because one is reversed so that if it is palindrome, then it should be same

#code:
def copy_list(head):
    copy_node = head
    fake_head = ListNode(None)
    curr = fake_head
    while copy_node is not None:
        curr.next = ListNode(copy_node.value)
        curr = curr.next
        copy_node = copy_node.next
    return fake_head.next
def reverse_linkedlist(head):
    prev = ListNode(None)
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr 
        curr = new_node
    return prev
def palindrome_check(head):
    copy = copy_list(head)
    new_linkedlist = reverse_linkedlist(copy)
    while head is not None and new_linkedlist is not None:
        if head.value == new_linkedlist.value:
            head = head.next
            new_linkedlist = new_linkedlist.next
        else:
            return False
    return True
    
    
        
