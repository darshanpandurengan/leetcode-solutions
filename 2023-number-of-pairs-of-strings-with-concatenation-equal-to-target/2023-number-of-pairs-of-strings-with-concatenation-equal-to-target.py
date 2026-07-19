class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        count = 0 
        #Brute force solution O(n^2) 
        for idx1 , num1 in enumerate(nums) :
            for idx2 , num2 in enumerate(nums) :
                if idx1 != idx2 and num1 + num2 == target :
                    count += 1 
        return count