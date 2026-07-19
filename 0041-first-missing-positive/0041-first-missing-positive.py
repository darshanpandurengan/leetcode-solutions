class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for num in nums :
            if num > 0 :
                s.add(num)
        print(s)
        for i in range(1, len(nums) + 1 ) :
            if i not in s :
                return i
        return len(nums) + 1 