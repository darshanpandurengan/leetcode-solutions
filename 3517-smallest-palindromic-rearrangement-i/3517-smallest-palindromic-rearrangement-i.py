class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = [0] * 26
        front = rev = mid = ""
        for ch in s :
            freq[ord(ch) - ord("a")] += 1 
        for idx , count in enumerate(freq) :
            front += chr(idx + ord("a")) * ( count // 2 ) 
            rev = chr(idx + ord("a")) * ( count // 2 ) + rev
            if count % 2 == 1 and count > 0 :
                mid = chr(idx + ord("a")) 
        return front + mid + rev 

