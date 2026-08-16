class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = float('-inf')
        secondlargest = float('-inf')
        minimum = float('inf')
        for num in nums:
            if num > largest:
                secondlargest = largest
                largest = num
            elif num > secondlargest:
                secondlargest = num
            if num < minimum:
                minimum = num
        return largest + secondlargest - minimum