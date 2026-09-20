class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        for i in range(1 , len(l) , 2) :
            l[i] = chr(ord(l[i - 1]) + int(l[i]))
        return "".join(l)