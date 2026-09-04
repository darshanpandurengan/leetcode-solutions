class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = list(s) 
        vowels = [] 
        for letter in letters :
            if letter in "aeiouAEIOU" :
                vowels.append(letter) 
        vowels.sort() 
        if not vowels :
            return "".join(letters) 
        j = 0 
        for i in range(len(letters)) :
            if letters[i] in "aeiouAEIOU" : 
                letters[i] = vowels[j]
                j += 1 
        return "".join(letters)