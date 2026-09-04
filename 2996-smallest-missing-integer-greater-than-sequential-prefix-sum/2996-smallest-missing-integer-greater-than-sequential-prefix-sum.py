class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [nums[0]] 
        for i in range(1 , len(nums)) :
            if nums[i] != prefix[i -1] + 1 :
                break 
            else :
                prefix.append(nums[i])
        arraySum = sum(prefix) 
        while True :
            if arraySum not in nums :
                return arraySum 
            arraySum += 1 
        