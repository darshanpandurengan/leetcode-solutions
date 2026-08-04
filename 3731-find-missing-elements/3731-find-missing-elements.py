class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        mn = min(nums)
        mx = max(nums) 
        for i in range(mn + 1 , mx ) :
            if i not in nums :
                res.append(i)
        return res