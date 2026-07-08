class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted(nums)
        def searchLeftSide(nums) :
            pos = -1 
            left , right = 0 , len(nums) - 1 
            while left <= right :
                mid = (left + right) // 2 
                if nums[mid] == target :
                    pos =  mid
                    right = mid - 1 
                elif nums[mid] < target : 
                    left = mid + 1 
                else : 
                    right = mid - 1 
            return pos
        def searchRightSide(nums) :
            pos = -1 
            left , right = 0 , len(nums) - 1 
            while left <= right :
                mid = (left + right) // 2 
                if nums[mid] == target :
                    pos =  mid
                    left = mid + 1 
                elif nums[mid] < target : 
                    left = mid + 1 
                else : 
                    right = mid - 1 
            return pos
        lowerBound = searchLeftSide(nums)
        if lowerBound == -1 :
            return [] 
        upperBound = searchRightSide(nums)
        return [i for i in range(lowerBound , upperBound + 1 ) ] 