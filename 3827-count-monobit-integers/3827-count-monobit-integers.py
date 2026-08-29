class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0 
        for i in range(n + 1 ) :
            if len(set(bin(i)[2 : ])) == 1 :
                res += 1 
        return res