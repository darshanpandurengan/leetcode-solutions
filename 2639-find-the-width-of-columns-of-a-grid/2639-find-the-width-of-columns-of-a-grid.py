class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        row = len(grid) 
        col = len(grid[0])
        res = [] 
        for j in range(col) :
            max_digit = 0
            for i in range(row) :
                num = grid[i][j]
                max_digit = max(max_digit ,len(str(num)) )
            res.append(max_digit)
        return res