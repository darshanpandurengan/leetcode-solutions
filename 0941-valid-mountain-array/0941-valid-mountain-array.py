class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3 :
            return False
        peak_index = 1
        for i in range(2 , len(arr) - 1) :
            if arr[i] > arr[peak_index] :
                peak_index = i
        if  peak_index  == len(arr) - 1 :
            return False
        for i in range(1 , peak_index + 1) :
            if arr[i - 1] >= arr[i] :
                return False
        for i in range(peak_index  , len(arr) - 1) :
            if arr[i] <= arr[i + 1] :
                return False
        return True 