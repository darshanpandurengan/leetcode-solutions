class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0 
        for row in grid :
            row.sort(reverse = True) 
        for i in range(len(grid[0])) :
            curr_max = 0
            for j in range(len(grid)) :
                curr_max = max(curr_max , grid[j][i]) 
            res += curr_max
        return res