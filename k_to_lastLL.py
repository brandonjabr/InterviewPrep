def k_to_lastLL(k,head):
    curr = head
    length = 0

    while curr:
        length += 1
        curr = curr.next
    
    curr = head
    length -= k

    while length > 0:
        curr = curr.next
        length -= 1

    return curr

class LinkedListNode:
    
    def __init__(self,value):
        self.value = value
        self.next = None


h = LinkedListNode(3)

h.next = LinkedListNode(5)

h.next.next = LinkedListNode(7)