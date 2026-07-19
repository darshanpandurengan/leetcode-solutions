class Solution(object):
    def rearrangeString(self, s, x, y):
        """
        :type s: str
        :type x: str
        :type y: str
        :rtype: str
        """
        d = {}
        for ch in s :
            if ch not in d :
                d[ch] = 1 
            else :
                d[ch] += 1 
        res = ""
        for ch in set(y) :
            if ch in d :
                res += ch * d[ch]
                d[ch] = 0 
        for ch in set(x) :
            if ch in d :
                res += ch * d[ch]
                d[ch] = 0 
        for k , v in d.items() :
            res += k * v 
        return res    