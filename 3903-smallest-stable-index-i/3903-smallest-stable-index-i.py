class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)) :
            mx = float("-inf")
            mn = float("inf") 
            for j in range(0 , i + 1) :
                mx = max(mx , nums[j]) 
            for l in range(i , len(nums)) :
                mn = min(mn , nums[l]) 
            if mx - mn <= k :
                return i 
        return -1