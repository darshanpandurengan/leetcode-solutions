class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0 
        product = 1 
        temp = n 
        while n :
            digit = n % 10 
            sum += digit 
            product *= digit 
            n = n // 10 
        return temp % (sum + product) == 0 