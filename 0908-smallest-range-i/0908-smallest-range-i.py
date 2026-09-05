class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(nums) 
        mn = min(nums) 
        if mx == mn :
            return 0 
        for i in range(k) :
            mx -= 1 
            mn += 1 
            if mn >= mx :
                return 0 
        return mx - mn            