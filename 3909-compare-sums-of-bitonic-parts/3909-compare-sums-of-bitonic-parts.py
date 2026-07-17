class Solution(object):
    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peak_index = -1 
        for i in range(1 , len(nums) - 1) :
            if nums[i - 1] <  nums[i] > nums[ i + 1 ] :
                peak_index = i 
                break 
        ascending_sum = sum(nums[: peak_index + 1 ])
        descending_sum = sum(nums[peak_index : ])
        if ascending_sum > descending_sum :
            return 0 
        elif ascending_sum < descending_sum :
            return 1
        return -1