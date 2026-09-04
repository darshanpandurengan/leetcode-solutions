class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        for num in nums :
            res += min(1 , num % 3 )
        return res