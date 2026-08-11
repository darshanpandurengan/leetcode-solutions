class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def extractdigits(str) :
            sum = 0 
            for ch in str :
                sum += int(ch)
            return sum
        res = ""
        for ch in s :
            res += str( (ord(ch) - ord("a") + 1) )
        temp = 0 
        for _ in range(k) :
            temp = extractdigits(res)
            res = str(temp)
        return temp