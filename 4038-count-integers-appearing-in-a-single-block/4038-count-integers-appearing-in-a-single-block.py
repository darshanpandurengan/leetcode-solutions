class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set() 
        invalid = set() 
        prev = None 
        for num in nums :
            if prev != num :
                if num in seen :
                    invalid.add(num)
                else :
                    seen.add(num) 
            prev = num
        return len(seen) - len(invalid)