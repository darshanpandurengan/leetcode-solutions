class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_element = max(nums)
        return k * max_element + (k - 1) * (k) // 2 