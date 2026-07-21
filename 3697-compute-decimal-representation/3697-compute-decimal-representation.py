class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [] 
        countor = 1 
        while n :
            temp = n % 10 
            if temp != 0 :
                res.append(temp * countor)
            countor *= 10
            n = n // 10 
        return res[::-1]
            
