class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ans = sum(nums[i] for i in range(k))
        temp = ans
        for i in range(k , len(nums)) :
            temp += nums[i] - nums[i - k]
            ans = max(temp , ans)
        return ans / float(k)        