class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set() 
        res = None
        for num in nums :
            if num in seen :
                if res is None :
                    res = num 
                else :
                    res = res ^ num 
            seen.add(num)
        if res is None :
            return 0 
        return res