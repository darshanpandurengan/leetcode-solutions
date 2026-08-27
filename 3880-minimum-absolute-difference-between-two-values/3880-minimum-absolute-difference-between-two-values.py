class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("inf") 
        for idx1 , num1 in enumerate(nums) :
            for idx2 , num2 in enumerate(nums) :
                if idx1 != idx2 and num1 == 1 and num2 == 2 :
                    res = min(res , abs(idx1 - idx2))
        if res == float("inf") :
            return -1 
        return res