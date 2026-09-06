class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 10 :
            return False
        countor = 1 
        temp = 10 
        while n > 0 :
            n -= temp
            temp -= 1 
            if n < temp :
                if countor == 1  :
                    return True 
                else :
                    return False
            countor = 1 - countor 
        return countor == 0 