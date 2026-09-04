class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(set(nums)) == 1 :
            return "equilateral"
        nums.sort() 
        if nums[0] + nums[1] <= nums[2] :
            return "none"
        if len(set(nums)) == 3 :
            return "scalene"
        return "isosceles"