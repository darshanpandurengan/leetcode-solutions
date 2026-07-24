class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = [0] * 1001
        for num in arr1 :
            count[num] += 1 
        res = [] 
        for num in arr2 :
            res.extend([num] * count[num])
            count[num] = 0 
        for num , freq in enumerate(count) :
            res.extend([num] * freq)
        return res