class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        prev = grid[0]
        for i in range(1 , len(grid)) :
            if prev != grid[i] :
                return False
        temp = grid[0]
        prev = temp[0] 
        for i in range(1 , len(temp)) :
            if prev == temp[i] :
                return False
            prev = temp[i]
        return True