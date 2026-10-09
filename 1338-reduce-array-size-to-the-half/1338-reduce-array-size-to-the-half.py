class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        size = len(arr) // 2 
        d = {}
        for num in arr :
            if num in d :
                d[num] += 1 
            else :
                d[num] = 1 
        res = 0 
        freq = [] 
        for v in d.values() :
            freq.append(v)
        freq.sort(reverse = True) 
        for num in freq :
            size -= num
            res += 1 
            if size <= 0 :
                return res 
        return res