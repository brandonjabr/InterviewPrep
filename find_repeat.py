# Given a list of n+1 numbers from 1..n, find the one that appears twice, using O(1) additional space.

def find_repeat(nums):
    # Use sum(1..n) = (n**2 + n) / 2 (Triangular Series)
    n = len(nums) - 1
    maxVal = (n**2 + n) / 2

    return sum(nums) - maxVal