class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = str(n) + str(2 * n) + str(3 * n) 
        if "0" in num :
            return False
        if len(set(num)) != 9 or len(num) != 9 :
            return False
        return True