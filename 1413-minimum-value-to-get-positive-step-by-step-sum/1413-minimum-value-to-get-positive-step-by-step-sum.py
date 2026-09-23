class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1 , len(nums)) :
            nums[i] = nums[i] + nums[i - 1] 
        startValue = min(nums) 
        if startValue > 0 :
            return 1 
        return abs(startValue) + 1 