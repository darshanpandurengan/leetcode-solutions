class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            "(" : ")" ,
            "{" : "}" ,
            "[" : "]"
        }
        stack =[] 
        for i in s :
            if i in "({[" :
                stack.append(i)
            elif stack and i == d[stack[-1]]:
                stack.pop()
            else :
                return False
        return not stack