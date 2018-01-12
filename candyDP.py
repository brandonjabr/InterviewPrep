def candy(ratings):
    A = ratings[:]
    n = len(ratings)
    res = [1]*n
    for i in range(1,n):
        if A[i] > A[i-1]:
            res[i] = res[i-1]+1
    for i in range(n-2,-1,-1):
        if A[i] > A[i+1] and res[i] <= res[i+1]:
            res[i] = res[i+1]+1
    return sum(res)