class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = {}
        for ch in words[0] :
            if ch not in  d :
                d[ch] = 1 
            else :
                d[ch] += 1 
        for i in range(1 , len(words)) :
            temp = {} 
            for ch in words[i] :
                if ch  in d :
                    if ch not in temp :
                        temp[ch] = 1 
                    else :
                        temp[ch] += 1 
            for k , v in list(d.items()) :
                if k not in temp :
                    del d[k] 
                else :
                    d[k] = min(d[k] , temp[k]) 
        res = [] 
        for k , v in d.items() :
            res.extend([k] * v)
        return res