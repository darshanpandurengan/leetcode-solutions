class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [] 
        for ch in s :
            if stack :
                if stack[-1] == "A" and ch == "B" :
                    stack.pop() 
                elif stack[-1] == "C" and ch == "D" :
                    stack.pop()
                else :
                    stack.append(ch)
            else :
                stack.append(ch)
        return len(stack)