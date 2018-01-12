# Find 3 values in A whose sum is closest to integer B (V. Hard)
def threeSumClosest(A, B):
    A.sort()
    n=len(A)
    res = float('inf')
    
    for i in xrange(0,n-2):
        
        left = i+1
        right = n-1

        while left<right:
            
            s = A[i] + A[left] + A[right]
               
            if abs(res-B) > abs(s-B):
                res = s
            if s == B:
                return B
            if s > B:
                right-=1
            else:
                left+=1
    return res