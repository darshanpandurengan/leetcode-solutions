class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() 
        count = 0 
        for num in nums[:-1] :
            count += nums[-1] - num
        return count