class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negativeCount , positiveCount = 0 , 0 
        for num in nums :
            if num  < 0 :
                negativeCount += 1 
            elif num > 0 :
                positiveCount += 1 
        return max(negativeCount , positiveCount)