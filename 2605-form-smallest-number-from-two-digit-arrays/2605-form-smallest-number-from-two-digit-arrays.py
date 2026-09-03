class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        for i in range(1 , 10) :
            if i in nums1 and i in nums2 :
                return i 
        nums1.sort()
        nums2.sort() 
        return min(nums1[0] , nums2[0]) * 10 + max(nums1[0] , nums2[0])