class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Brute Force
        def countVowels(word) :
            count = 0 
            for ch in word :
                if ch in "aeiou" :
                    count += 1 
            return count
        words = s.split(" ")
        vowel_count = countVowels(words[0])
        for i in range(1 , len(words)) :
            if vowel_count == countVowels(words[i]) :
                words[i] = words[i][::-1]
        return " ".join(words)