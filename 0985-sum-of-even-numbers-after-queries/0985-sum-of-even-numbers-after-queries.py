class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        original_even_sum = 0 
        for num in nums :
            if num % 2 == 0 :
                original_even_sum += num
        res = [] 
        for val , idx in queries :
            if nums[idx] % 2 == 0 :
                if val % 2 == 0 :
                    original_even_sum += val           
                else :
                    original_even_sum -= nums[idx]
            else :
                if val % 2 == 1 :
                    original_even_sum += nums[idx] + val
            res.append(original_even_sum)
            nums[idx] += val
        return res