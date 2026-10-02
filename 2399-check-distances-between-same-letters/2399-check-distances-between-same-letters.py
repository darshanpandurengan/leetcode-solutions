class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        d = {} 
        for i , ch in enumerate(s) :
            if ch not in d :
                d[ch] = [] 
            d[ch].append(i) 
        def isEqullaySpace(arr , val) : 
            for i in range(1 , len(arr)) :
                if arr[i] - arr[i -1] - 1  != val :
                    return False
            return True 
        for idx , val in enumerate(distance) :
            ch = chr(ord("a") + idx)
            if ch  not in d :
                continue 
            else :
                if isEqullaySpace(d[ch] , val ) :
                    continue 
                else :
                    return False
        return True 