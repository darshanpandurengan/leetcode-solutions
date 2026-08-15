class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        for num in nums :
            if num % 2 == 0 :
                res = res | num
        return res