def addTwoNumbers(l1, l2):

    carryOne = 0
    out = ListNode(0)
    rootOut = out
    
    while l1 and l2:
        nextVal = l1.val + l2.val + carryOne
            
        if nextVal < 10:
            out.val = nextVal
            carryOne = 0
        else:
            out.val = nextVal - 10
            carryOne = 1
            
        l1 = l1.next
        l2 = l2.next
        out.next = ListNode(0)
        out = out.next
    
    # Add remaining digits of longer number
    if l1 and not l2:
        while l1:
            out.val = l1.val + carryOne
            if not l1.next:
                break
            out.next = ListNode(0)
            out = out.next
            l1 = l1.next

    if l2 and not l1:
        while l2:
            out.val = l2.val + carryOne
            if not l2.next:
                break
            out.next = ListNode(0)
            out = out.next
            l2 = l2.next

    return rootOut


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

l1 = ListNode(3)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(6)

l2 = ListNode(4)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


"""
l1 = 3 -> 4 -> 3 -> 6
l2 = 4 -> 6 -> 4

out = -> 7 -> 0 -> 8 -> 6
"""
assert (printLL(addTwoNumbers(l1,l2)) == '7 -> 0 -> 8 -> 6')

"""
l1 = 3 -> 4 -> 9 -> 6
l2 = 4 -> 6 -> 4

out = -> 7 -> 0 -> 4 -> 7
"""
l1.next.next.val = 9
assert (printLL(addTwoNumbers(l1,l2)) == '7 -> 0 -> 4 -> 7')

