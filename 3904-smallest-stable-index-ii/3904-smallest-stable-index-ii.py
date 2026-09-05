class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        min_array = [0] * n 
        min_array[n - 1] = nums[-1] 
        for i in range(n - 2 , -1 , -1 ) :
            min_array[i] = min(nums[i] , min_array[i + 1]) 
        max_element = nums[0] 
        for i in range(n) :
            max_element = max(max_element , nums[i])
            if max_element - min_array[i] <= k :
                return i 
        return -1