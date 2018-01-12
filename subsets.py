def subs(nums):
    res = [[]]

    for num in nums:
        res += [item + [num] for item in res]
    return res

def subsBinary(A):
    result = []
    for i in range(0,2**len(A)):
        binary = bin(i)[2:] 
        binary = '0'*(len(A)-len(binary)) + binary
        subset = [ A[i] for i,x in enumerate(binary) if x=='1' ]
        print binary,subset
        result.append(subset)
    print result