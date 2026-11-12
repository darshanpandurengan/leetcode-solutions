class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1 
        increasing = 1
        decreasing = 1 
        prev = nums[0] 
        for i in range(1 , len(nums)) :
            if nums[i] > prev :
                increasing += 1 
            else :
                increasing = 1 
            if nums[i] < prev :
                decreasing += 1 
            else :
                decreasing = 1 
            prev = nums[i] 
            res = max(res ,decreasing ,increasing)
        return res