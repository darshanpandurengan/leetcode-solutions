class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m * n != len(original) :
            return []
        res = []
        for i in range(0 , len(original) , n ) :
            temp = original[i : i + n ] 
            res.append(temp)
        return res