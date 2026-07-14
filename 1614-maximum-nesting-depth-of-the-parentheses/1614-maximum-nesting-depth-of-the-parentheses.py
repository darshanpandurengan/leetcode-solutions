class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        output , countor = 0 , 0 
        for i in s :
            if i == "(" :
                countor += 1 
                output = max(output , countor)
            elif i == ")" and countor >= 0 :
                countor -= 1 
        return output