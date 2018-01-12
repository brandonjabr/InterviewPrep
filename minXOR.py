def findMinXOR(A):
    minVal = float("Inf")
    A = sorted(A)
    for i in xrange(len(A)-1):
        minVal = min(minVal,A[i]^A[i+1])
    return minVal

print findMinXOR([0,2,3,4])