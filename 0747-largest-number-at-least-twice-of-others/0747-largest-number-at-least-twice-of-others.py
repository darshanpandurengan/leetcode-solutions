class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Finding largetest and second largest 
        largest = float("-inf")
        second_largest = float("-inf")
        largest_index = -1
        for idx , num in enumerate(nums) :
            if num > largest :
                second_largest = largest
                largest = num 
                largest_index = idx
            elif num > second_largest :
                second_largest = num 
        if largest >= 2 * second_largest :
            return largest_index 
        return -1