class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        def isThere(roots , word) :
            res = word 
            for root in roots :
                if word.startswith(root) :
                    if len(root) < len(res) :
                        res = root 
            return res
        words = sentence.split(" ") 
        for i in range(len(words)) :
            words[i] = isThere(dictionary , words[i])
        return " ".join(words)