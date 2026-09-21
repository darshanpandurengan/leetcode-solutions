class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        
        for row in nums :
            row.sort() 
        Score = 0 
        for i in range(len(nums[0])) :
            rowMAX = 0 
            for j in range(len(nums)) :
                rowMAX = max(rowMAX , nums[j][i] ) 
            Score += rowMAX
        return Score