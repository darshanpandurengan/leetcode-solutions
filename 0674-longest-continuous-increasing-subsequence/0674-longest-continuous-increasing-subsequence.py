class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        temp = 1 
        for i in range( 1 , len(nums)) :
            if nums[i] > nums[i - 1] :
                temp += 1 
            else :
                temp = 1 
            if temp > res :
                res = temp 
        return res