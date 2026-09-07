class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("inf")
        n = len(nums) 
        for i in range(n) :
            for j in range(i + 1 , n ) :
                if nums[i] == nums[j] :
                    for k in range(j + 1 , n ) :
                        if nums[j] == nums[k] :
                            res = min(res , 2 * (k - i)) 
        if res == float("inf") :
            return -1 
        return res