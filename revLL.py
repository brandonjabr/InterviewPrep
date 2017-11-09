def revLL(head):
    current = head
    nxt = None
    prev = None

    while current:
        nxt = current.next

        current.next = prev

        prev = current
        current = nxt

    return prev

class LinkedListNode:
    
    def __init__(self,value):
        self.value = value
        self.next = None


h = LinkedListNode(3)

h.next = LinkedListNode(5)

h.next.next = LinkedListNode(7)


