class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        num = int(num)
        while num :
            digit = num % 10 
            if digit % 2  == 1 :
                return str(num)
            num = num // 10 
        return ""