#problem description:
    #create a basic element of linkedlist - listnode
    
#code:
class ListNode():
    def __init__(self,value):
        self.next = None    #havent decide what the next node is
        self.value = value
        
#example:
'''
node1 = ListNode('a')
node2 = ListNode('b')
node1.next = node2 #we can change the parameter outside the class. this is actually creating a two node linkedlist
'''
