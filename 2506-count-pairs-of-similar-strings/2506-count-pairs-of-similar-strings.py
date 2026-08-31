class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {} 
        for word in words  :
            temp = "".join(sorted(set(word)))
            if temp in d :
                d[temp] += 1 
            else :
                d[temp] = 1 
        res = 0 
        for v in d.values() :
            res += v * (v - 1) // 2 
        return res