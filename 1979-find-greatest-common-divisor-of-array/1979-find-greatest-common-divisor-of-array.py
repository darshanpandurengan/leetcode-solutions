class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a , b) :
            while b :
                a , b = b , a % b 
            return abs(a)
        nums.sort()
        return gcd(nums[-1] , nums[0])