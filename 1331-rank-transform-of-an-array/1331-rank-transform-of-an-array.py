class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """        
        temp = sorted(set(arr))
        rank = {value : (idx + 1)  for idx , value in enumerate(temp)}
        res = []
        for num in arr :
            res.append(rank[num])
        return res