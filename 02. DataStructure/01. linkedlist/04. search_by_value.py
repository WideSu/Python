#problem description:
    #given a value, return it

#code:
def search_by_value(head,value):
    if not head:
        return None
    while head is not None:
        if head.value == value:
            return head
        else:
            head = head.next
    return None
