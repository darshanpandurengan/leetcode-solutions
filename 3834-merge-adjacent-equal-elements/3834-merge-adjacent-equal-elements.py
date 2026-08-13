class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = [] 
        for num in nums :
            stack.append(num)
            while len(stack) >= 2 and stack[-1] == stack[-2] :
                stack.pop() 
                stack[-1] = 2 * stack[-1]
        return stack    