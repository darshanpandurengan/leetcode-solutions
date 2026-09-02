class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = s.count("1")
        zero = s.count("0")
        return (ones - 1) * "1" + zero * "0" + 1 * "1"