class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = len(s) - 1 
        res = ""
        while i >= 0 :
            if s[i] != "#" :
                res += chr(int(s[i]) - 1 + ord("a"))
                i -= 1 
            else :
                res += chr(int(s[i - 2 : i] ) - 1 + ord("a") )
                i -= 3 
        return res[::-1]
