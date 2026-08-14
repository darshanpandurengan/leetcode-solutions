class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0 
        right_sum = sum(nums) 
        for idx , num in enumerate(nums) :
            right_sum -= num 
            if left_sum == right_sum :
                return idx 
            left_sum += num 
        return -1