class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s :
            if stack :
                if stack[-1].isupper() and ch.islower() :
                    if stack[-1] == ch.upper() :
                        stack.pop()
                    else :
                        stack.append(ch)
                elif stack[-1].islower() and ch.isupper() :
                    if stack[-1] == ch.lower() :
                        stack.pop()
                    else :
                        stack.append(ch)
                else :
                    stack.append(ch)
            else :
                stack.append(ch)
        return "".join(stack)