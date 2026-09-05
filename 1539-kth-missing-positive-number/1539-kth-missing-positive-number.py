class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        left , right = 0 , len(arr) 
        while left < right :
            mid = (left + right) // 2 
            if (arr[mid] - (mid + 1  )) >= k  : 
                right = mid
            else :
                left = mid + 1 
        return left + k