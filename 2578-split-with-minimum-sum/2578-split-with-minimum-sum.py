class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = [] 
        while num :
            arr.append(num % 10)
            num = num // 10 
        arr.sort() 
        num1 = num2 = 0
        countor = 0 
        for num in arr :
            if countor == 0 :
                num1 = num1 * 10 + num 
            else :
                num2 = num2 * 10 + num 
            countor = 1 - countor 
        return num1 + num2 