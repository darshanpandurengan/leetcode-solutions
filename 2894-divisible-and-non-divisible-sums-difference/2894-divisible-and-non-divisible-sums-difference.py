class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        total_sum = n * (n + 1) // 2 
        num2 = 0 
        for i in range(m , n + 1 , m) :
            num2 += i 
        return total_sum - 2 * num2