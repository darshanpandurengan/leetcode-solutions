class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans1 = 0 
        ans2 = 0 
        temp1 = set(nums1)
        temp2 = set(nums2)
        for num in nums1 :
            if num in temp2 :
                ans1 += 1
        for num in nums2 :
            if num in temp1 :
                ans2 += 1 
        return [ans1 , ans2]