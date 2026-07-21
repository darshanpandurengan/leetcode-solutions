class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        single = double = 0 
        for num in nums :
            if num < 10 :
                single += num
            else :
                double += num 
        return single != double
        