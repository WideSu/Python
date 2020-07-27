#problem description:
    #given an index, we want to add a new listnode befor that node.
    
#idea:
    #if the node is the head, we just need to connect the new node with the head.
    #if it is not the head, we need to connect with the last one and the next one.
    #a more advanced method is to first add a new null node as the head and we do not need to discuss whether the index is head or not.
    
#code:
#method1:
def add_to_index(head,index,value):
    if not head or index < 0:
        return None
    if index = 0:
        new_node = ListNode(value)
        new_node.next = head
        return new_node
    else:
        prev_node = search_by_index(head,index-1):   #when use this function, should first change its return from head.value to head. because here, we want an object not an integer.
        if prev_node is None:
            return None
        new_node = ListNode(value)
        new_node.next = prev_node.next
        prev_node.next = new_node
    return head
#method2:
def add_to_index_fakehead(head,index,value):
    if not head or index < 0:
        return None
    fake_head = ListNode(None)
    fake_head.next = head
    prev_node = search_by_index(fake_head,index) #no need for index-1 since we add one already so index is same with index-1 in original linkedlist
    if prev_node == None:
        return None
    new_node = ListNode(value)
    new_node.next = prev_node.next
    prev_node.next = new_node
    return fake_head.next
