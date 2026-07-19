class Solution(object):
    def isDigitorialPermutation(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def factorial(num) :
            if num <= 1 :
                return 1 
            return num * factorial(num - 1 )
        if n == 0 :
            return False
        temp = n
        count = 0 
        while temp :
            count += factorial(temp % 10)
            temp = temp // 10 
        return sorted(str(count)) == sorted(str(n))