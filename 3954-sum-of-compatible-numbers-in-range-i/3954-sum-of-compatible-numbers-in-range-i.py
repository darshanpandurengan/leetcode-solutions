class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        sum = 0 
        for i in range(1 , n + k + 1) :
            if n & i == 0 and abs(n - i) <= k :
                sum += i 
        return sum