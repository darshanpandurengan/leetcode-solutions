class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0 
        count = 0 
        for num in nums[:-1] :
            left_sum += num 
            total_sum -= num 
            if left_sum % 2 == 0 and total_sum % 2 == 0:
                count += 1 
            elif left_sum % 2 == 1 and total_sum % 2 == 1:
                count += 1 
        return count