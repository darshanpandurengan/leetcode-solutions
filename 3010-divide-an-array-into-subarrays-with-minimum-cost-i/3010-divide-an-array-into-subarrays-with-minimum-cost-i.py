class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn1 = float("inf")
        mn2 = float("inf")
        for num in nums[1: ] :
            if num < mn1 :
                mn2 = mn1 
                mn1 = num 
            elif num < mn2 :
                mn2 = num 
        return nums[0] + mn1 + mn2