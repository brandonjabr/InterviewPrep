# @param A : list of integers
# @return an integer
def bulbs(A):
    presses = 0
    for n in xrange(len(A)):
        if A[n] == 0:
            A[n] = 1
            A[n+1:] = [x^1 for x in A[n+1:]]
            presses += 1
            if sum(A) == len(A):
                return presses
    return presses

