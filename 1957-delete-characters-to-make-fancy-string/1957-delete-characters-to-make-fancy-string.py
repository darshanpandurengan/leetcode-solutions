class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 3 :
            return s 
        res = [] 
        res.append(s[0]) 
        res.append(s[1]) 
        for i in range(2 , len(s)) :
            if res[-1] == res[-2] == s[i] :
                continue 
            else :
                res.append(s[i])
        return "".join(res)