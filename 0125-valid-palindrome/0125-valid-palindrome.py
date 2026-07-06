class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower() 
        res = ""
        for ch in s :
            if ch.isalnum() :
                res += ch
        return res == res[::-1]