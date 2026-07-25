class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [] 
        while n :
            res.append(n % 10)
            n = n // 10
        res.sort()
        return res[-1] * res[-2]