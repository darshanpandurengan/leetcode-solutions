class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        res = [] 
        temp = ""
        countor = 0 
        for ch in s :
            countor += 1 
            temp += ch 
            if countor % k == 0 :
                res.append(temp)
                temp = ""
        if temp :
            res.append(temp + (k - len(temp)) * fill)
        return res