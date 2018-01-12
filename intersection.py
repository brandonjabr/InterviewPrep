
def intersect(A, B):
    res=[]
    i,j = 0,0
    sizeA, sizeB = len(A), len(B)
    
    while i<sizeA and j<sizeB:
        
        if (A[i] > B[j]):
            j += 1
        elif (B[j] > A[i]):
            i += 1
        else:
            res.append(A[i])
            i, j = i+1, j+1

    return res