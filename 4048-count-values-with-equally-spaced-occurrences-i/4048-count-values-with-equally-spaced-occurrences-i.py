class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)) :
            if nums[i] not in d :
                d[nums[i]] = [] 
            d[nums[i]].append(i)
        res = 0 
        print(d)
        for v in d.values() :
            if len(v) == 3 and v[2] + v[0] == 2 * v[1] :
                res += 1 
        return res