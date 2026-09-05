class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        seen = set(nums)
        res = 0 
        for i in range(n) :
            for j in range(i + 1 , n ) :
                for k in range(j + 1 , n ) :
                    temp = nums[i] + nums[j] + nums[k]
                    if temp in seen :
                        for l in range(k + 1 , n) :
                            if temp == nums[l] :
                                res += 1 
        return res