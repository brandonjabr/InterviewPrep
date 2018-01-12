def removeDuplicates(A):
    if len(A) == 1:
        return 1
    
    lastVal = A[-1]
    for i in xrange(len(A)-2,-1,-1):
        if A[i] == lastVal:
            lastVal = A.pop(i)
        else:
            lastVal = A[i]
    return A

print removeDuplicates([0,0,0,1,1,2,3,5,7,7])
