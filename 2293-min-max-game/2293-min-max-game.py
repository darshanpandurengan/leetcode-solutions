class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countor = 0 
        size = len(nums)
        while size > 1 :
            newNums = [] 
            for i in range(0 , size , 2) :
                if countor == 0 :
                    newNums.append(min(nums[i] , nums[i + 1])) 
                else :
                    newNums.append(max(nums[i] , nums[i + 1])) 
                countor = 1 - countor 
            nums = newNums 
            size = size // 2 
        return nums[0]