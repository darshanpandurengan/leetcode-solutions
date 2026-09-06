class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        d = {}
        for a , b in dominoes :
            temp = (a , b)
            if temp in d :
                d[temp] += 1 
            elif temp[::-1] in d :
                d[temp[::-1]] += 1 
            else :
                d[temp] = 1 
        res = 0 
        for v in d.values() :
            res += v * (v - 1) // 2 
        return res