class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digitsum = 0 
        squaresum = 0 
        while n :
            digit = n % 10 
            digitsum += digit 
            squaresum += digit * digit 
            n = n // 10 
        return squaresum - digitsum >= 50 