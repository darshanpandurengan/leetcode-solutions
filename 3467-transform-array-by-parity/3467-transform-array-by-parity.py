class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = 0 
        for num in nums :
            if num % 2 == 0 :
                even += 1 
        return [0] * even + [1] * (len(nums) - even)