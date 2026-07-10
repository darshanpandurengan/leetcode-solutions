class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        return str(x) != str(n)[0] and str(n).count(str(x)) > 0 