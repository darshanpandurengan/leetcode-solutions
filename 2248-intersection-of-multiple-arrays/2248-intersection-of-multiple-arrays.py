class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        d = {}
        for num in nums[0] :
            if num not in d :
                d[num] = 1 
        for num in nums[1 : ] :
            for n in num :
                if n in d :
                    d[n] += 1 
        res = []
        for k , v in d.items() :
            if v == len(nums) :
                res.append(k)
        res.sort() 
        return res