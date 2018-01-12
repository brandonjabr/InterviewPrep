from collections import Counter
def kLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    return heapq.nlargest(k, nums)[k-1
            
nums = [3,2,1,5,6,4]

print kMostCommon(nums,2)