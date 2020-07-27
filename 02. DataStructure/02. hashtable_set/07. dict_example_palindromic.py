#problem description:
    #words like 'aaabaaa'

#palindrome in linkedlist:
#basic idea is have one linkedlist and then reverse it to get a new one. Then have a traverse to check whether value equal or not.

#code:
def copy_list(head):
    fake_head = ListNode(None)
    new_list = fake_head
    curr = head
    while curr is not None:
        new_list.next = ListNode(curr.value)
        curr = curr.next
        new_list = new_list.next
    return fake_head.next
def reverse_linkedlist(head):
    prev = ListNode(None)
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
def check_palindrome(head):
    copy = copy_list(head)
    head2 = reverse_linkedlist(copy)
    while head1 and head2:
        if head1.value == head2.value:
            head1 = head1.next
            head2 = head2.next
        else:
            return False
    return True
    
#what if the input is a string or list?
    '''
    there are the following situations:
        if the word or list contains even number of element, for each distinct element, it must appear at an even frequency.
        if the word or list contains odd number of element, only one element can appear at an odd frequency.
        example:
            aabbcc -> even number -> each distinct element appear twice(even)
            aabcc -> odd numver -> only one element(b) appear once(odd)
    ultimate conclusion, no matter even or odd, the largest number of odd frequency is 1
    so, we can put all distinct element into one dict and use its value to count its frequency
    '''

#code:
def check_palindrome(word):
    freq = {}
    for i in word:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    odd_count = 0
    for value in freq.values():
        if value % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return False
    return True

#complexity:
#time: O(n)
#sapce: O(c) #c is the distinct element in word
