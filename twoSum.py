def twoSum(nums, target):
        
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for k in d.keys():
            comp = target - k
            if comp in d:
                return [d[k],d[comp]]
        return False