from collections import Counter
def kMostFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    return zip(*Counter(nums).most_common(k))[0]
            
nums = [1,1,1,2,2,3]

print kMostFrequent(nums,2)