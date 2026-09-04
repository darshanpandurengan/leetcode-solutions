class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for word in words :
            if word in d :
                d[word] += 1 
            else :
                if word[::-1] in d :
                    d[word[::-1]] += 1
                else :
                    d[word] = 1 
        res = 0 
        for v in d.values() :
            res += v * (v - 1) // 2 
        return res