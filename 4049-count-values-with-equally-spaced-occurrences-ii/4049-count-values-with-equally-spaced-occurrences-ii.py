class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i , num in enumerate(nums) :
            if num not in d :
                d[num] = [] 
            d[num].append(i)
        res = 0 
        def isEquallySpaced(arr) :
            gap = arr[1] - arr[0] 
            for i in range(1 , len(arr)) :
                if arr[i] - arr[i - 1] != gap :
                    return False
            return True 
        for v in d.values() :
            if len(v) > 2 and isEquallySpaced(v) :
                res += 1 
        return res