class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = float("inf") 
        countor = 0 
        for row in grid :
            left = 0 
            right = len(row) - 1 
            while left < right :
                if row[left] != row[right] :
                    countor += 1 
                left += 1 
                right -= 1 
        res = min(res , countor) 
        countor = 0 
        rows = len(grid) - 1 
        for i in range(len(grid[0])) :
            left = 0 
            right = rows
            while left < right  :
                if grid[left][i] != grid[right][i] :
                    countor += 1 
                left += 1 
                right -= 1 
        return min(res , countor)