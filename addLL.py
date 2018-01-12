def addTwoNumbers(A, B):
    aVal,bVal = '',''
    
    while A or B:
        if A:
            aVal += str(A.val)
            A = A.next
        if B:
            bVal += str(B.val)
            B = B.next
    
    target = str(int(aVal[::-1]) + int(bVal[::-1]))
    
    curr = ListNode(int(target[-1]))
    root = curr
    for char in target[::-1][1:]:
        curr.next = ListNode(int(char))
        curr = curr.next
    return root


class ListNode:
    
    def __init__(self,val):
        self.val = val
        self.next = None

def printLL(l):
    ll_str = ""
    while l:
        ll_str += str(l.val)
        if l.next:
            ll_str += " -> "
        l = l.next
    return ll_str

A = ListNode(3)
A.next = ListNode(4)
A.next.next = ListNode(3)
A.next.next.next = ListNode(6)

B = ListNode(4)
B.next = ListNode(6)
B.next.next = ListNode(4)


"""
A = 3 -> 4 -> 3 -> 6
B = 4 -> 6 -> 4

out = -> 7 -> 0 -> 8 -> 6
"""
assert (printLL(addTwoNumbers(A,B)) == '7 -> 0 -> 8 -> 6')

"""
A = 3 -> 4 -> 9 -> 6
B = 4 -> 6 -> 4

out = -> 7 -> 0 -> 4 -> 7
"""
A.next.next.val = 9
assert (printLL(addTwoNumbers(A,B)) == '7 -> 0 -> 4 -> 7')

