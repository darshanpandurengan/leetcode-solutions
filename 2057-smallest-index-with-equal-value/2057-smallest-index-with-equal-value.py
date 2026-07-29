class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx , num in enumerate(nums) :
            if idx % 10 == num :
                return idx 
        return -1