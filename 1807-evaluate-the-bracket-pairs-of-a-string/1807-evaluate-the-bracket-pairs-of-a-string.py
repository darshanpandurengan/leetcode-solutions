class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = {key : value for key , value in knowledge} 
        temp = ""
        res = [] 
        for ch in s :
            if ch == "(" :
                temp += "(" 
            elif ch == ")" :
                key = temp[1 : ]
                temp = ""
                if key not in d :
                    res.append("?") 
                else :
                    res.append(d[key])
            else :
                if temp :
                    temp += ch 
                else :
                    temp = ""
                    res.append(ch) 
        return "".join(res)