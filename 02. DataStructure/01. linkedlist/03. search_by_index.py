#problem description:
    #given an index, we search for its value

#idea:
    #return value
    #out of index then stop

#code:
def search_by_index(head,index):
    if head is None or head < 0:
        return None
    for i in range(index):
        head = head.next
        if not head:
            return None
    return head.value
