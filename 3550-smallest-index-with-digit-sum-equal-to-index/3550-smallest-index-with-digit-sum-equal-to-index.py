class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digitsum(num) :
            digit_sum = 0 
            while num :
                digit_sum += num % 10 
                num = num // 10
            return digit_sum 
        for idx , num in enumerate(nums) :
            if idx == digitsum(num) :
                return idx
        return -1