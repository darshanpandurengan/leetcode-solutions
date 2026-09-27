class Solution(object):
    def minQueenMoves(self, source, target):
        """
        :type source: List[int]
        :type target: List[int]
        :rtype: int
        """
        if source == target :
            return 0 
        if source[0] == target[0] or source[1] == target[1] :
            return 1  # horizontal and vertical moves 
        # diagonal move
        if  abs(source[0] - target[0]) == abs(source[1] - target[1]) :
            return 1 
        return 2 