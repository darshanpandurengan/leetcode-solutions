class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for num in nums :
            if num not in d :
                d[num] = 1 
            else :
                d[num] += 1 
        pair = 0 
        leftover = 0 
        for v in d.values() :
            pair += v // 2 
            leftover += v % 2 
        return [pair , leftover]