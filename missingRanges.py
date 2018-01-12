    def findMissingRanges(nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper:
                return [str(upper)]
            else:
                return [str(lower)+'->'+str(upper)]
        
        ranges = []
        
        r = (lower, nums[0])
        if r[1] > r[0] + 1:
            ranges.append(str(r[0])+'->'+str(r[1]-1))
        if r[1] == r[0] + 1:
            ranges.append(str(r[0]))
        
        lastVal = nums[0]
        for i in range(1,len(nums)):
            r = (lastVal+1, nums[i])
            print r
            if r[1] > r[0] + 1:
                ranges.append(str(r[0])+'->'+str(r[1]-1))
            if r[1] == r[0] + 1:
                ranges.append(str(r[0]))
            lastVal = nums[i]

        r = (nums[-1]+1, upper)
        if r[1] > r[0]:
            ranges.append(str(r[0])+'->'+str(r[1]))
        if r[1] == r[0]:
            ranges.append(str(r[1]))
    
        return ranges

nums = [0,1,3,50,75]