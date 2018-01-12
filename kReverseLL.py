def reverseList(A, B):
    
    count = 0
    curr = A
    prev = None
    start = A
    while curr.next:
        if count <= B-1:
            if count == 0:
                start = curr
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            count += 1
        else:
            tmp = curr.next
            start.next = curr
            start = curr
            prev = curr
            curr = tmp
            count = 0
    return A

class LinkedListNode:
    
    def __init__(self,value):
        self.value = value
        self.next = None


h = LinkedListNode(3)

h.next = LinkedListNode(5)

h.next.next = LinkedListNode(7)

reverseList(h,3)