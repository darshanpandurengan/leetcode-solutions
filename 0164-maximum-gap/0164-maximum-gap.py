class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 :
            return 0 
        nums.sort() 
        res = -1 
        for i in range(len(nums) - 1) :
            res = max(res , nums[i + 1] - nums[i])
        return res