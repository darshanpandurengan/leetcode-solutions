class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sorting Method
        temp = list(nums)
        temp.sort() 
        if temp[-1] >= 2 * temp[-2] :
            return nums.index(temp[-1])
        return -1