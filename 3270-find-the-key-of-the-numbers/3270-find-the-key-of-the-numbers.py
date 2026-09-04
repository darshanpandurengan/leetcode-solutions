class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        res = 0 
        place = 1 
        for _ in range(4) :
            res += place * min(num1 % 10 , num2 % 10 , num3 % 10)
            num1 = num1 // 10
            num2 = num2 // 10
            num3 = num3 // 10
            place *= 10 
        return res