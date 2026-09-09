class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        countor = 0
        for ch in s[::-1] :
            if ch != "-" :
                res += ch.upper()
                countor += 1 
                if countor % k == 0 :
                    res += "-"
        if res and res[-1] == "-" :
            return res[::-1][1:]
        return res[::-1]