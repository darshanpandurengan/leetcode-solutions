class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def compare(d1 , d2) :
            for k , v in d1.items() :
                if k not in d2 :
                    return False
                else :
                    if v > d2[k] :
                        return False
            return True 
        d = {}
        for ch in licensePlate.lower() :
            if ch.isalpha() :
                if ch in d :
                    d[ch] += 1 
                else :
                    d[ch] = 1 
        res = None
        for word in words :
            f = {}
            for ch in word :
                if ch in f :
                    f[ch] += 1 
                else :
                    f[ch] = 1 
            if compare(d, f):
                if res is None or len(word) < len(res):
                    res = word
        return res