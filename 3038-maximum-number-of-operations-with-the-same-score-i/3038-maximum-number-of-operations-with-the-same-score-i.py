class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        score =  nums[0] + nums[1] 
        i = 0 
        while i + 1 < len(nums) :
            if nums[i] + nums[i + 1] != score :
                break 
            res += 1 
            i += 2 
        return res