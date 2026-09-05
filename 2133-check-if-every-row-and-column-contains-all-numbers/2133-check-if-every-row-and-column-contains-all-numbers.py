class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix) 
        total_sum = n * (n + 1) // 2 
        for row in matrix :
            if sum(row) != total_sum or len(set(row)) != n :
                return False
        transposed = [list(row) for row in zip(*matrix)]
        for col in transposed :
            if sum(col) != total_sum or len(set(col)) != n :
                return False
        return True