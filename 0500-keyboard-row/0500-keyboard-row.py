class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def isSameRow(row , word) :
            word = set(word.lower() )
            for ch in word :
                if ch not in row :
                    return False
            return True
        res = [] 
        f_row = "qwertyuiop"
        s_row = "asdfghjkl"
        t_row =  "zxcvbnm"
        for word in words :
            if (isSameRow(f_row ,word) or isSameRow(s_row,word) or isSameRow(t_row, word)):
                res.append(word)
        return res 