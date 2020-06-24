#problem description:
    #traverse all nodes in the linkedlist and print their value

#idea:
    #head is the most important node because once we know it, we know all nodes behind it
    #we can stop the loop when their is no next which means next = None

#code:
def traverse_linkedlist(head):
    while head is not None:
        print (head.value)
        head = head.next

#use traverse to find number of nodes:
def find_total_number(head):
    if head is None:
        return 0
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count
