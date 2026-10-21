class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = [] 
        n = 0
        for num in nums :
            n = 2 * n 
            if num == 1 :
                n += 1 
            if n % 5 == 0 :
                res.append(True) 
            else :
                res.append(False)
        return res