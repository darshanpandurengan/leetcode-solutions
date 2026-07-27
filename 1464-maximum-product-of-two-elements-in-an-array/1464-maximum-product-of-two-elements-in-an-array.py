class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = max(nums) - 1
        nums.remove(product + 1)
        product*=(max(nums)-1)
        return product