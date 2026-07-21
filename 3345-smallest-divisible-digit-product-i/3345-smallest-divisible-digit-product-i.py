class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digitproducts(num) :
            if num == 0 :
                return 0 
            temp = 1 
            while num :
                temp *= num % 10 
                num = num // 10 
            return temp
        while (digitproducts(n) % t ) :
            n += 1 
        return n
        