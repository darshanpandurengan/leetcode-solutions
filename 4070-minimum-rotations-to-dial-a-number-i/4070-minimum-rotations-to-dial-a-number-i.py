class Solution(object):
    def minRotations(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0 
        prev = 0
        for d in s :
            digit = int(d) 
            res += min( abs(prev - digit) , 10 - abs(digit - prev ) )
            prev = digit 
        return res 