class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]] 
        for num in nums[1:] :
            prefix.append(num + prefix[-1])
        return prefix