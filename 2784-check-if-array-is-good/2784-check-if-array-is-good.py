class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        base = [i for i in range(1 , len(nums))] + [len(nums) - 1] 
        nums.sort() 
        return nums == base
        