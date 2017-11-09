class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        if not A:
            return -1
        start, end = 0, len(A) - 1
        
        while start <= end:
            mid = start + (end - start) / 2

            if A[mid] == B:
                return mid
            
            if A[mid] > A[start]:
                if A[start] <= B and A[mid] > B:
                    end = mid
                else:
                    start = mid
            
            elif A[mid] < A[start]:
                if A[mid] < B and A[end] >= B:
                    start = mid
                else:
                    end = mid
            
            else:
                start += 1

        if A[start] == B:
            return start
        if A[end] == B:
            return end
        return -1