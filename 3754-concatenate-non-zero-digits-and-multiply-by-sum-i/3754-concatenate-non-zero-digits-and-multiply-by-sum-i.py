class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        add , digits = 0 , 0
        while n :
            temp = n % 10 
            if temp != 0 :
                add += temp
                digits = digits * 10 + temp
            n = n // 10  
        return add * int(str(digits)[::-1])