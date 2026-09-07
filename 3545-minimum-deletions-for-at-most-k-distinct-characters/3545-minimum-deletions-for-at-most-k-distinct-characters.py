class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = [0] * 26 
        for ch in s :
            freq[ord(ch) - ord("a")] += 1 
        freq.sort()
        n = freq.count(0)
        if 26 - n <= k :
            return 0 
        k = 26 - n - k
        res = 0 
        for i in range(n , 26) :
            res += freq[i]
            k -= 1 
            if k == 0 :
                return res
        return res