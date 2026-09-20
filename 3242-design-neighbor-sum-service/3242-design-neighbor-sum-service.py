class NeighborSum(object):

    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.grid = grid 
        self.d = {}
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                self.d[grid[i][j]] = [i , j] 
        self.size = len(grid)

    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        res = 0 
        i , j = self.d[value] 
        if i > 0 :
            res += self.grid[i - 1][j]
        if i < self.size - 1 :
            res += self.grid[i + 1][j]
        if j > 0 :
            res += self.grid[i][j - 1]
        if j < self.size - 1 :
            res += self.grid[i][j + 1]
        return res 

    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        res = 0 
        i , j = self.d[value]
        if i  > 0  : 
            if j  > 0 :
                res += self.grid[i - 1][j - 1] 
            if j + 1 < self.size :
                res += self.grid[i - 1][j + 1] 
        if i  < self.size - 1 :
            if j  > 0 :
                res += self.grid[i + 1][j - 1] 
            if j + 1 < self.size :
                res += self.grid[i + 1][j + 1]
        return res 


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)