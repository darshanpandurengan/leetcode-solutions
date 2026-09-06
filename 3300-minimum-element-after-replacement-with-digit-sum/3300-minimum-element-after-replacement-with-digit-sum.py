class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("inf") 
        for num in nums :
            sum = 0 
            while num :
                sum += num % 10 
                num = num // 10
            res = min(res , sum )
        return res