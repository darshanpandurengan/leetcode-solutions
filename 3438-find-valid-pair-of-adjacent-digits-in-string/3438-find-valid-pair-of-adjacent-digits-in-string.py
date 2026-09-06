class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {str(i) : 0 for i in range(1, 10) }
        for i in s :
            d[i] += 1 
        for i in range(len(s) - 1):
            a = s[i]
            b = s[i + 1]
            if a != b and d[a] == int(a) and d[b] == int(b):
                return a + b
        return ""