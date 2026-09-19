class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        nums.sort() 
        left = 0 
        right = len(nums) - 1 
        while left < right :
            temp = nums[left] + nums[right] 
            if temp > res :
                res = temp 
            left += 1 
            right -= 1 
        return res