def maxOnes(A, B):
    bestCount = 0
    bestStart = 0
    
    i = j = curNumZeroes = 0
    while i <= j < len(A):
        if A[j] == 0:
            curNumZeroes += 1
        
        while curNumZeroes > B:
            if A[i] == 0:
                curNumZeroes -= 1
            i += 1
            
        if j - i + 1 > bestCount:
            bestCount = j - i + 1
            bestStart = i
            
        j += 1
            
    return [i for i in range(bestStart, bestStart + bestCount)]

print maxOnes([0,1,1,1,0],1)