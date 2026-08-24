class Solution(object):
    def isPalindromic(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ""
        for ch in s :
            asci_value = ord(ch)
            binary = bin(asci_value)[2  : ]
            temp = "0" * (8 - len(binary)) + binary 
            res += temp 
        return res == res[::-1]
        