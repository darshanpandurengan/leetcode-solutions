class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        d = {val : idx for idx , val in enumerate(nums)} 
        for original , replace in operations :
            idx = d[original] 
            nums[idx] = replace 
            d[replace] = idx 
        return nums