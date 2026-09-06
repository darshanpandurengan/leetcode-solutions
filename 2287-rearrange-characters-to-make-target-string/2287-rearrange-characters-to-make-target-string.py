class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        freq = [0] * 26 
        for ch in target :
            freq[ord(ch) - ord("a")] += 1 
        res = float("inf")
        d = [0] * 26 
        for ch in s :
            d[ord(ch) - ord("a")] += 1 
        for ch in set(target) :
            idx = ord(ch) - ord("a")
            if d[idx] > 0 :
                res = min(res , d[idx] // freq[idx]) 
            else :
                return 0
            if res == 0 :
                return 0 
        return res
