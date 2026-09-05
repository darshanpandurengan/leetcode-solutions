class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = [0] * 26 
        for ch in s :
            freq[ord(ch) - ord("a")] += 1 
        res = ""
        while (max(freq) != 0 ) :
            for i in range(26) :
                if freq[i] > 0 :
                    res += chr(ord("a") + i) 
                    freq[i] -= 1 
            for i in range(25 , -1 , -1) :
                if freq[i] > 0 :
                    res += chr(ord("a") + i ) 
                    freq[i] -= 1 
        return res