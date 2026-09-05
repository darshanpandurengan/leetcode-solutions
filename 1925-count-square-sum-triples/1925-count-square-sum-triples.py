class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0 
        for a in range(1 , n + 1) :
            for b in range(1 , n + 1) :
                c_square = a * a + b * b 
                c = int(c_square ** 0.5) 
                if c <= n and c * c == c_square :
                    res += 1 
        return res    