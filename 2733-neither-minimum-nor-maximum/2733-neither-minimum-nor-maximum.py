class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums) )
        nums.sort() 
        if len(nums) < 3 :
            return -1
        return nums[1]