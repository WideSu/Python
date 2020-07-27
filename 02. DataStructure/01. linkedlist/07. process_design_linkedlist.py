class ListNode():
    def __init__(self,value):
        self.next = None
        self.value = value

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self,index):
        if index < 0 or index >= self.size:
            return None
        node = self.head
        for i in range(index):
            node = node.next
            if node == None:
                retunr None
        return node
    
    def get_val(self,index):
        if index < 0 or index >= self.size:
            return None
        node = self.head
        for i in range(index):
            node = node.next
            if node == None:
                return None
        return node.value
    
    def add_at_head(self,value):
        if self.size == 0:
            self.head = self.tail = ListNode(value)
        else:
            new_head = ListNode(value)
            new_head.next = self.head
            self.head = new_head
        self.size += 1
    
    def add_at_tail(self,value):
        if self.size == 0:
            self.head = self.tail = ListNode(value)
        else:
            new_tail = ListNode(value)
            self.tail.next = new_tail
            sel.tail = new_tail
        self.size += 1
    
    def add_at_index(self,index,value):
        if index < 0 or index > self.size:
            return None
        if index == 0:
            self.add_at_head(value)
        elif index == self.size:
            self.add_at_tail(value)
        else:
            prev_node = self.get(index - 1)
            new_node = ListNode(value)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
    
    def remove_at_index(self,index,value):
        if index < 0 or index >= self.size:
            return None
        if index == 0:
            new_head = self.head.next
            self.head = new_head
            self.size -= 1
        elif index == self.size - 1:
            new_tail = self.get(index - 1)
            new_tail.next = None
            self.tail = new_tail
            self.size -= 1
        else:
            prev_node = get(index - 1)
            remove_node = prev_node.next
            prev_node.next = remove_node.next
            remove_node.next = None
            self.size -= 1
            
