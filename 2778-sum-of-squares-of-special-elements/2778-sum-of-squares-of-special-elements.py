class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        n = len(nums) 
        for idx , val in enumerate(nums) :
            if n % (idx + 1 ) == 0 :
                res += val * val 
        return res