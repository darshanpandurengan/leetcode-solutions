class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        res = 0 
        for i in range(limit + 1) :
            for j in range(limit + 1) :
                for k in range(limit + 1) :
                    if i + j + k == n :
                        res += 1
        return res