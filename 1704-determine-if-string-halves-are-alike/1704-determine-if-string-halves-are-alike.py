class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def calculateVowel(word):
            count = 0 
            word = word.lower() 
            for ch in word :
                if ch in "aeiou" :
                    count += 1 
            return count
        return calculateVowel(s[:len(s) // 2 ]) == calculateVowel(s[len(s) // 2 : ])