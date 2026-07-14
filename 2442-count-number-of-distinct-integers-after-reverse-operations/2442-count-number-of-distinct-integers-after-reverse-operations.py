class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        print(nums)
        for num in set(nums) :
            s.add(int(str(num)[::-1]))
        return len(s)