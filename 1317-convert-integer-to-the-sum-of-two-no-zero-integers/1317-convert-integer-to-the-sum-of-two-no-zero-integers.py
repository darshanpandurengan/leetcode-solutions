class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def containsZero(num) :
            if num == 0 :
                return False
            while num :
                if num % 10 == 0 :
                    return False
                num = num // 10 
            return True
        for i in range(1 , n) :
            if containsZero(i) and containsZero(n - i) :
                return [i , n - i] 
        return [-1 , -1]      