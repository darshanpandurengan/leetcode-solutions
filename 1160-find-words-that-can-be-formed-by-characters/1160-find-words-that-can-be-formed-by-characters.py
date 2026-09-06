class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        def compare(d1 , d2) :
            for k , v in d2.items() :
                if k not in d1 :
                    return False
                if v > d1[k] :
                    return False
            return True 
        d = {} 
        for ch in chars :
            if ch not in d :
                d[ch] = 1 
            else :
                d[ch] += 1 
        count = 0 
        for word in words :
            f = {}
            for ch in word :
                if ch not in f :
                    f[ch] = 1 
                else :
                    f[ch] += 1 
            if compare(d , f ) :
                count += len(word) 
        return count