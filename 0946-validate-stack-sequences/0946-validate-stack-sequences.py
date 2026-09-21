class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        res = []
        i = 0 
        for val in pushed :
            res.append(val) 
            while res and i < len(popped) and res[-1] == popped[i] :
                res.pop()
                i += 1 
        return not res