class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == len(nums) :
            return 0 
        nums.sort() 
        n = len(nums)
        res = 0  
        for i in range(k) :
            res += nums[n - i - 1] - nums[i]
        return res