class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = [] 
        i = 1 
        for num in target :
            while (num != i) :
                stack.extend(["Push","Pop"])
                i += 1 
            stack.append("Push")
            i += 1 
        return stack