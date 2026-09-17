class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        noOflines = 1 
        curr = 0
        for ch in s :
            temp = widths[ord(ch) - ord("a")]
            if temp + curr > 100 :
                curr = temp 
                noOflines += 1 
            else :
                curr += temp 
        return [noOflines , curr]