class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0 
        sign = 1 
        for digit in str(n) :
            res += int(digit) * sign 
            sign *= -1 
        return res