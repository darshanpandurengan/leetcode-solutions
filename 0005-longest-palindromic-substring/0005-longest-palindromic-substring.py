class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Brute force Approach 
        left = 0  
        right = 0 
        max_size = 1
        n = len(s)
        for i in range(n) :
            for j in range(i + 1 , n ) :
                if(j - i + 1 > max_size and s[i : j + 1] == s[i : j + 1][::-1]) :
                    left = i 
                    right = j 
                    max_size = j - i + 1 
        return s[left : right + 1]