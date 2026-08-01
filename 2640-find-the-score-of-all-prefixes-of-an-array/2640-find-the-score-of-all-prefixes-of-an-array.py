class Solution(object):
    def findPrefixScore(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_element = nums[0] 
        for i in range(len(nums)) :
            if max_element < nums[i] :
                max_element = nums[i]
            if i > 0 :
                nums[i] += nums[i-1] + max_element 
            else :
                nums[i] += nums[i]
        return nums